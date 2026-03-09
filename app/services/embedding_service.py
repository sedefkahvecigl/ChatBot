import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

class EmbeddingService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY bulunmadı. Lütfen .env dosyasını kontrol et.")
        
        self.client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta'})

    def get_embeddings(self, text:str):
        try:
            result = self.client.models.embed_content(
                model="gemini-embedding-001",
                contents=text, 
            )
            return result.embeddings[0].values
        except Exception as e:
            print(f"[EMBEDDING] Hata: {e}")
            return None
        
if __name__ == "__main__":
    service = EmbeddingService()
    test_vektor = service.get_embeddings("Merhaba dünya!")
    if test_vektor:
        print(f"başarılı! vektör uzunluğu: {len(test_vektor)}")
        print(f"ilk 5 sayı: {test_vektor[:5]}")