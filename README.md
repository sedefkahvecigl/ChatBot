GEMİNİ-RAG CHATBOT: AKILLI PDF ANALİZ SİSTEMİ

Bu proje; karmaşık PDF belgelerini işlemek, tabloları anlamlandırmak ve Google Gemini modellerini kullanarak bu belgeler hakkında bağlama duyarlı yanıtlar sunmak için geliştirilmiş bir Retrieval-Augmented Generation (RAG) asistanıdır.

ÖNE ÇIKAN ÖZELLİKLER


Gelişmiş Tablo İşleme: pdfplumber ile tabloları Markdown formatına dönüştürerek LLM'in veri yapısını anlamasını sağlar.

Akıllı Parçalama (Smart Chunking): Paragraf ve cümle bütünlüğünü koruyan özyinelemeli metin bölme.

Vektör Arama: Milyonlarca veri arasında benzerlik araması için Milvus (Vector Database) entegrasyonu.

Streamlit Arayüzü: Dosya yükleme ve gerçek zamanlı sohbet imkanı sunan modern UI.

TEKNOLOJİ YIĞINI


Dil Modeli (LLM): Google Gemini SDK

Vektör Veritabanı: Milvus (Docker üzerinde)

Metin İşleme: pdfplumber

Arayüz: Streamlit

Programlama: Python 3.12+

PROJE YAPISI


<img width="636" height="327" alt="image" src="https://github.com/user-attachments/assets/50dac110-414a-40c8-80e6-b2e540d9756c" />

KURULUM VE ÇALIŞTIRMA


1. Ön Koşullar

Docker & Docker Compose.

Google AI Studio API Key.

2. Altyapıyı Başlatma

cd deploy

docker-compose up -d

3. Python Ortamı

cd ..

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

4. Başlatma

python app/database/milvus_manager.py

streamlit run streamlit_app.py


KULLANIM SENARYOSU

PDF Yükleme: Sidebar panelinden PDF dosyasını seçin.

Hafızaya Öğret: "Hafızaya Öğret" butonuna basarak dokümanı indeksleyin.

Sorgulama: Belgedeki tablolara veya metinlere dair sorular sorun.


🛡️ Lisans

Bu proje eğitim amaçlı geliştirilmiş bir açık kaynak projesidir.
