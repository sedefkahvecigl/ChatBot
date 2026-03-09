import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.database.milvus_manager import MilvusManager
from app.services.embedding_service import EmbeddingService
from pymilvus import Collection

class DataManager:
    def __init__(self):
        self.db = MilvusManager()
        self.embedding_service = EmbeddingService()
        self.collection_name = "chatbot_memory"

    def save_to_memory(self, text:str):
        try:
            self.db.connect()
            self.db.create_schema() 
            self.db.create_index()   
            
            vector = self.embedding_service.get_embeddings(text)

            if vector:
                collection = Collection(name=self.collection_name)
                
                data = [[text], [vector]]

                collection.insert(data)
                collection.flush()
                print(f"[DATA MANAGER] hafızaya kaydedildi: '{text}'")
            else:print("[DATA MANAGER] vektör oluşturulamadı.")
        except Exception as e:
            print(f"[DATA MANAGER] kayıt hatası: {e}")

if __name__ == "__main__":
    manager = DataManager()
    manager.save_to_memory("Stajyerler chatbot geliştirebilirler.") 