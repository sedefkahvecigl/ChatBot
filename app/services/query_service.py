import sys
from pathlib import Path

# Workspace kök dizinini path'e ekle
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from pymilvus import Collection, connections
from app.services.embedding_service import EmbeddingService
from app.database.milvus_manager import MilvusManager

class QueryService:
    def __init__(self):
        self.db = MilvusManager()
        self.embedding_service = EmbeddingService()
        self.collection_name = "chatbot_memory"

    def search_similar(self, query_text: str, limit: int = 5):
            try:
                self.db.connect()
                
                self.db.create_index()
                
                query_vector = self.embedding_service.get_embeddings(query_text)

                collection = Collection(self.collection_name)
                collection.load()
                search_params = {"metric_type": "L2","params": {"nprobe": 10}}

                results = collection.search(
                    data=[query_vector],
                    anns_field="embeddings",
                    param=search_params,
                    limit=limit,
                    output_fields=["text"]
                )

                found_texts = []
                for hits in results:
                    for hit in hits:
                        found_texts.append(hit.entity.get("text"))
                return found_texts
            except Exception as e:
                print(f"[QUERY SERVICE] Arama hatası: {e}")
                return []

if __name__ == "__main__":
    qs = QueryService()
    sonuclar = qs.search_similar("Stajyerler")
    print("\nbotun hafızasında neler var?")
    for i, txt in enumerate(sonuclar, 1):
        print(f"{i}. {txt}")