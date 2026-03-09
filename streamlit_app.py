import streamlit as st
import os
import sys
from pathlib import Path

# Proje ana dizinini yola ekle (Import hatalarını önlemek için)
PROJECT_ROOT = str(Path(__file__).parent)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.main import chatbotAgent
from app.services.pdf_manager import PDFManager

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="AI BilgiAsistanı", page_icon="🤖", layout="wide")

# --- ASİSTAN VE PDF YÖNETİCİSİ BAŞLATMA ---
@st.cache_resource
def get_agent():
    return chatbotAgent()

@st.cache_resource
def get_pdf_manager():
    return PDFManager()

agent = get_agent()
pdf_manager = get_pdf_manager()

# --- YAN PANEL (SIDEBAR) ---
with st.sidebar:
    st.title("📂 Veri Yönetimi")
    st.subheader("Yeni Bilgi Ekle")
    uploaded_file = st.file_uploader("Bir PDF dosyası yükleyin", type="pdf")
    
    if uploaded_file is not None:
        # Dosyayı geçici olarak kaydet
        if not os.path.exists("temp_data"):
            os.makedirs("temp_data")
        
        file_path = os.path.join("temp_data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Hafızaya Öğret 🧠"):
            with st.spinner("PDF analiz ediliyor ve Milvus'a işleniyor..."):
                pdf_manager.process_pdf(file_path)
                st.success(f"✅ {uploaded_file.name} başarıyla hafızaya eklendi!")

# --- ANA SOHBET EKRANI ---
st.title("AI Bilgi Asistanı")
st.markdown("Hafızamdaki belgelere dayanarak sorularınızı yanıtlıyorum.")

# Sohbet geçmişini tutmak için (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Geçmiş mesajları ekrana bas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı girişi
if prompt := st.chat_input("Sorunuzu buraya yazın..."):
    # Kullanıcı mesajını ekle ve göster
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot cevabını üret ve göster
    with st.chat_message("assistant"):
        with st.spinner("Hafıza taranıyor ve cevap üretiliyor..."):
            response = agent.ask(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})