import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from google import genai
from app.services.query_service import QueryService

load_dotenv()

class chatbotAgent:
    def __init__(self):
        self.query_service = QueryService()
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    def ask(self, user_query: str):
        context_docs = self.query_service.search_similar(user_query, limit=2)
        context_text = "\n".join(context_docs)

        prompt = f"""sen kurumsal bir asistansın. aşağıdaki bilgilere dayanarak kullanıcıın sorusunu yanıtla. eğer bilgi aşağıda yoksa, 'bu konuda hafızamda bir bilgi bulamadım' de.
        {context_text}
        {user_query}"""

        try:
            response = self.client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"cevap üretilirken hata oluştu: {e}"
        
if __name__ == "__main__":
    bot = chatbotAgent()
    print("Merhaba! Sorularınızı sorabilirsiniz. Çıkmak için 'exit' yazın.")

    while True:
        user_input = input("\nSiz:")
        if user_input.lower() =='exit':
            break

        print("düşünüyor...")
        answer = bot.ask(user_input)
        print(f"Bot: {answer}")
