import PyPDF2
import ollama
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Désactiver les logs httpx
logging.getLogger("httpx").setLevel(logging.WARNING)

class OllamaChat:
    def __init__(self, model: str = 'llama3.2'):
        self.model = model
        self.client = ollama.Client(host='http://localhost:11434')
        self.conversation = [{'role': 'system', 'content': 'Tu es un assistant intelligent. Tu réponds aux questions en fonction du contexte fourni de manière courte et concise.'}]

    def add_user_message(self, message: str):
        self.conversation.append({'role': 'user', 'content': message})

    def get_ai_response(self) -> str:
        try:
            response = self.client.chat(
                model=self.model, 
                messages=self.conversation,
                options={'temperature': 0.2}
            )
            ai_message = response['message']['content']
            self.conversation.append({'role': 'assistant', 'content': ai_message})
            return ai_message
        except Exception as e:
            logger.error(f"Erreur lors de la génération de la réponse : {e}")
            return "Je suis désolé, une erreur s'est produite."

    def interactive_chat(self):
        print("\n🤖 L'IA est prête à répondre à vos questions - Tapez 'exit' pour quitter")
        print("--------------------------------------------------")
        while True:
            user_input = input("\n🧑 Vous : ")

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n🤖 Au revoir !")
                break

            self.add_user_message(user_input)
            print("\n🤖 Assistant : ", end='', flush=True)
            ai_response = self.get_ai_response()
            print(ai_response)

# Fonction pour extraire le texte du fichier PDF
def extract_text_from_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def main():
    file_path = './pdf/temp.pdf'
    
    extracted_text = extract_text_from_pdf(file_path)

    # Créer une session de chat Ollama
    chat = OllamaChat()
    
    chat.add_user_message(f"Voici le contenu du document que vous devez analyser : {extracted_text}")
    
    chat.interactive_chat()

if __name__ == '__main__':
    main()