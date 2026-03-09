import os
import re
import pdfplumber
from app.services.data_manager import DataManager

class PDFManager:
    def __init__(self):
        self.data_manager = DataManager()

    def smart_chunking(self, text, max_chars=3000):
        """Metni cümle ve paragraf bütünlüğünü bozmadan güvenli parçalara ayırır."""
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""

        for p in paragraphs:
            # Emniyet Kemeri: Eğer bir paragraf tek başına max_chars'tan büyükse
            if len(p) > max_chars:
                # Önceki birikmiş parçayı kaydet
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = ""
                
                # Dev paragrafı noktalardan (cümlelerden) böl
                sentences = p.split('. ')
                temp_chunk = ""
                for s in sentences:
                    if len(temp_chunk) + len(s) <= max_chars:
                        temp_chunk += s + ". "
                    else:
                        if temp_chunk:
                            chunks.append(temp_chunk.strip())
                        temp_chunk = s + ". "
                if temp_chunk:
                    current_chunk = temp_chunk # Kalan kısmı bir sonrakine devret
            
            # Normal paragraf ekleme mantığı
            elif len(current_chunk) + len(p) <= max_chars:
                current_chunk += p + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = p + "\n\n"
                
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks

    def table_to_markdown(self, table):
        """Tablo verisini Gemini'nin anlayacağı Markdown formatına çevirir."""
        if not table or not any(table): 
            return ""
        
        # Satır içindeki gizli alt satır karakterlerini temizle
        clean_table = [[str(cell).replace('\n', ' ') if cell else "" for cell in row] for row in table]
        
        header = clean_table[0]
        md_table = "| " + " | ".join(header) + " |\n"
        md_table += "| " + " | ".join("---" for _ in header) + " |\n"
        
        for row in clean_table[1:]:
            md_table += "| " + " | ".join(row) + " |\n"
        return md_table

    def process_pdf(self, pdf_path):
        """PDF'i okur, tabloları ayıklar ve Milvus'a kaydeder."""
        try:
            full_text = ""
            print(f"{os.path.basename(pdf_path)} okunuyor...")
            
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    # 1. Metni al
                    page_text = page.extract_text()
                    if page_text:
                        full_text += f"\n[SAYFA {i+1} METNİ]\n{page_text}\n"
                    
                    # 2. Tabloları al ve Markdown'a çevir
                    tables = page.extract_tables()
                    for j, table in enumerate(tables):
                        table_md = self.table_to_markdown(table)
                        if table_md:
                            full_text += f"\n[SAYFA {i+1} TABLO {j+1}]\n{table_md}\n"

            # Parçala
            chunks = self.smart_chunking(full_text)
            print(f"{len(chunks)} parça oluşturuldu. Milvus'a gönderiliyor...")

            # Kaydet
            for chunk in chunks:
                if len(chunk.strip()) > 20: # Çok kısa parçaları atla
                    self.data_manager.save_to_memory(chunk)
            
            print(f"{os.path.basename(pdf_path)} başarıyla hafızaya alındı!")

        except Exception as e:
            print(f"PDF İşleme Hatası: {e}")

if __name__ == "__main__":
    pdf_proc = PDFManager()
    # Dosya adını ve yolunu kontrol etmeyi unutma!
    pdf_proc.process_pdf("data/ornek.pdf")