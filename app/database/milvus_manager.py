from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, utility
import os

class MilvusManager:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = "19530"
        self.collection_name = "chatbot_memory"

    def connect(self):
        
        try:
            connections.connect("default", host=self.host, port=self.port)
            print(f"[DATABASE] Milvus bağlantısı {self.host}:{self.port} üzerinden kuruldu.")
        except Exception as e:
            print(f"[DATABASE] Bağlantı hatası: {e}")

    def create_schema(self):
    
        if utility.has_collection(self.collection_name):
            print(f"[DATABASE] {self.collection_name} koleksiyonu zaten mevcut.")
            return

        
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535), 
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=3072) 
        ]

        schema = CollectionSchema(fields, description="Chatbot hafıza koleksiyonu")
        Collection(name=self.collection_name, schema=schema)
        print(f"[DATABASE] {self.collection_name} koleksiyonu başarıyla oluşturuldu.")

    def create_index(self):
        try:
            self.connect()
            collection = Collection(self.collection_name)
            
            index_params = {
                "metric_type": "L2",
                "index_type": "IVF_FLAT",
                "params": {"nlist": 1024}
            }
            
            print(f"[DATABASE] {self.collection_name} için index oluşturuluyor...")
            collection.create_index(
                field_name="embeddings", 
                index_params=index_params
            )
            print("[DATABASE] Index başarıyla oluşturuldu.")
        except Exception as e:
            print(f"[DATABASE] Index hatası: {e}")

if __name__ == "__main__":
   
    db = MilvusManager()
    db.connect()
    from pymilvus import connections
    if connections.has_connection("default"):
        db.create_schema()
    else:
        print("Bağlantı kurulamadığı için şema oluşturma işlemi iptal edildi.")
    db.create_index()