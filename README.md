# Gemini-RAG Chatbot: Akıllı PDF Analiz Sistemi

Bu proje; karmaşık PDF belgelerini işlemek, tabloları anlamlandırmak ve **Google Gemini modellerini kullanarak** bu belgeler hakkında bağlama duyarlı yanıtlar sunmak için geliştirilmiş bir **Retrieval-Augmented Generation (RAG)** asistanıdır.

---

# Öne Çıkan Özellikler

### Gelişmiş Tablo İşleme
`pdfplumber` kullanılarak PDF içerisindeki tablolar **Markdown formatına dönüştürülür**. Böylece dil modeli tablo yapısını daha doğru anlayabilir.

### Akıllı Parçalama (Smart Chunking)
Metinler **paragraf ve cümle bütünlüğü korunarak** özyinelemeli şekilde bölünür.

### Vektör Arama
Milyonlarca veri arasında hızlı benzerlik araması yapmak için **Milvus Vector Database** kullanılır.

### Streamlit Arayüzü
Kullanıcıların PDF yükleyebildiği ve sistemle sohbet edebildiği **modern bir web arayüzü** sunar.

---

# Teknoloji Yığını

| Teknoloji | Açıklama |
|-----------|----------|
| **LLM** | Google Gemini SDK |
| **Vector Database** | Milvus |
| **PDF İşleme** | pdfplumber |
| **Arayüz** | Streamlit |
| **Programlama Dili** | Python 3.12+ |

---

# Proje Yapısı

```
chatbot_project/
├── app/
│   ├── database/
│   │   └── milvus_manager.py     # Koleksiyon şeması ve index yönetimi
│   ├── services/
│   │   ├── data_manager.py       # Veri akış yönetimi
│   │   ├── embedding_service.py  # Gemini Embedding API entegrasyonu
│   │   ├── pdf_manager.py        # PDF okuma ve tablo ayıklama
│   │   └── query_service.py      # Vektör benzerlik araması
│   └── main.py                   # Chatbot ana mantığı
├── deploy/
│   └── docker-compose.yaml       # Milvus Docker altyapısı
├── streamlit_app.py              # Web arayüzü girişi
├── requirements.txt              # Bağımlılıklar
└── README.md                     # Dökümantasyon
```

---

# Kurulum ve Çalıştırma

## 1️⃣ Ön Koşullar

Aşağıdaki araçların sisteminizde kurulu olması gerekir:

- Docker
- Docker Compose
- Google AI Studio API Key

---

## 2️⃣ Altyapıyı Başlatma

```bash
cd deploy
docker-compose up -d
```

---

## 3️⃣ Python Ortamı Oluşturma

```bash
cd ..

python -m venv venv
```

Mac / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 4️⃣ Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

---

## ▶️ Uygulamayı Başlatma

Milvus bağlantısını başlatın:

```bash
python app/database/milvus_manager.py
```

Ardından Streamlit uygulamasını çalıştırın:

```bash
streamlit run streamlit_app.py
```

---

# 📖 Kullanım Senaryosu

### 1️⃣ PDF Yükleme
Streamlit arayüzünde **Sidebar panelinden PDF dosyasını yükleyin.**

### 2️⃣ Hafızaya Öğret
**"Hafızaya Öğret"** butonuna basarak belgeyi vektör veritabanına indeksleyin.

### 3️⃣ Sorgulama
Belgedeki metinler veya tablolar hakkında sorular sorabilirsiniz.  
Sistem, vektör arama ve Gemini modeli kullanarak bağlama uygun yanıtlar üretir.

---

# 🛡️ Lisans

Bu proje **eğitim amaçlı geliştirilmiş açık kaynak bir projedir.**
