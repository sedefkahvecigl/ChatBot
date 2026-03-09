Gemini-RAG Chatbot: Akıllı PDF Analiz Sistemi
Bu proje; karmaşık PDF belgelerini (ilanlar, mali raporlar, teknik dokümanlar) işlemek, içindeki tabloları anlamlandırmak ve Google Gemini 2.5 modelini kullanarak bu belgeler hakkında kullanıcıya doğru, bağlam duyarlı yanıtlar sunmak için geliştirilmiş bir Retrieval-Augmented Generation (RAG) asistanıdır.

Öne Çıkan Özellikler
Gelişmiş Tablo İşleme: pdfplumber kullanarak PDF içindeki tabloları Markdown formatına dönüştürür. Bu sayede LLM, satır ve sütun ilişkilerini kaybetmeden karmaşık verileri analiz edebilir.

Akıllı Parçalama (Smart Chunking): Metinleri rastgele değil, paragraf ve cümle bütünlüğünü koruyacak şekilde özyinelemeli (recursive) olarak böler.

Yüksek Performanslı Vektör Arama: Milyonlarca veri parçası arasında milisaniyeler içinde benzerlik araması yapmak için Milvus (Vector Database) kullanır.

Modern Web Arayüzü: Streamlit ile kullanıcıların dosya yükleyebileceği ve gerçek zamanlı sohbet edebileceği etkileşimli bir panel sunar.

Teknoloji Yığını
Dil Modeli (LLM): Google Gemini SDK (Flash/Pro)

Vektör Veritabanı: Milvus (Docker üzerinde Standalone)

Metin İşleme: pdfplumber (Tablo çekme uzmanı)

Arayüz: Streamlit

Altyapı: Docker & Docker Compose

Veri Yönetimi: PyMilvus & Python 3.12+

Proje Yapısı

Plaintext

chatbot_project/
├── app/
│   ├── database/
│   │   └── milvus_manager.py  # Koleksiyon şeması ve index yönetimi
│   ├── services/
│   │   ├── data_manager.py    # Metni vektöre çevirme ve kaydetme
│   │   ├── pdf_manager.py     # PDF okuma, tablo ayıklama ve smart chunking
│   │   └── query_service.py   # Benzerlik araması (Vector Search)
│   └── main.py                # Chatbot ana mantığı (Gemini entegrasyonu)
├── deploy/
│   └── docker-compose.yaml    # Milvus altyapısı için Docker ayarları
├── streamlit_app.py           # Web arayüzü ana giriş dosyası
├── requirements.txt           # Gerekli Python kütüphaneleri
└── README.md                  # Proje dökümantasyonu
⚙️ Kurulum ve Çalıştırma
1. Ön Koşullar

Docker & Docker Compose kurulu olmalı.

Google AI Studio'dan alınmış bir API Key.

2. Altyapıyı Başlatma (Milvus)

Bash
cd deploy
docker-compose up -d
3. Python Ortamını Hazırlama

Bash
# Ana dizine dön
cd ..
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
4. Veritabanı Şemasını Oluşturma

Bash
python app/database/milvus_manager.py
5. Uygulamayı Başlatma

Bash
streamlit run streamlit_app.py
📖 Kullanım Senaryosu
PDF Yükleme: Sol taraftaki sidebar panelinden istediğiniz PDF'i (Örn: Erasmus Hareketlilik İlanı) yükleyin.

Hafızaya Öğret: "Hafızaya Öğret" butonuna basın. Sistem PDF'i sayfalarca tarar, tabloları ayıklar, parçalar ve Milvus'a indeksler.

Soru Sor: "Hangi ülkeler 1. grup hibe desteği alıyor?" gibi spesifik tablo soruları sorun.

Yanıt Al: Bot, Milvus'tan ilgili tablo parçasını getirir ve Gemini aracılığıyla size insan dilinde özetler.
