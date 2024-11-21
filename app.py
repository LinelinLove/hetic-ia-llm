import ollama
import logging
from typing import List, Dict

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OllamaChat:
    def __init__(self, model: str = 'llama3.2'):
        """
        Initialise une session de chat interactive avec Ollama
        """
        self.model = model
        self.client = ollama.Client(host='http://localhost:11434')
        self.conversation: List[Dict[str, str]] = [
            {
                'role': 'system', 
                'content': 'Tu es un assistant français sympathique et intelligent. Réponds de manière naturelle et concise.'
            }
        ]

    def add_user_message(self, message: str):
        """
        Ajoute le message de l'utilisateur à la conversation
        """
        self.conversation.append({
            'role': 'user', 
            'content': message
        })

    def get_ai_response(self) -> str:
        """
        Obtient la réponse de l'IA et l'ajoute à la conversation
        """
        try:
            response = self.client.chat(
                model=self.model, 
                messages=self.conversation,
                options={
                    'temperature': 0.7,  # Contrôle la créativité
                    'max_tokens': 300    # Limite la longueur de réponse
                }
            )
            
            ai_message = response['message']['content']
            self.conversation.append({
                'role': 'assistant', 
                'content': ai_message
            })
            
            return ai_message
        except Exception as e:
            logger.error(f"Erreur lors de la génération de la réponse : {e}")
            return "Je suis désolé, une erreur s'est produite."

    def interactive_chat(self):
        """
        Lance une session de chat interactive dans le terminal
        """
        print("🤖 Assistant Ollama - Tapez 'exit' pour quitter")
        print("-----------------------------------")

        while True:
            try:
                # Demander l'entrée utilisateur
                user_input = input("\n🧑 Vous : ")
                
                # Option de sortie
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\n🤖 Au revoir !")
                    break
                
                # Ajouter le message de l'utilisateur
                self.add_user_message(user_input)
                
                # Obtenir et afficher la réponse
                print("\n🤖 Assistant : ", end='', flush=True)
                ai_response = self.get_ai_response()
                print(ai_response)

            except KeyboardInterrupt:
                print("\n\n🤖 Chat interrompu. Tapez 'exit' pour quitter.")
            except Exception as e:
                logger.error(f"Erreur durant le chat : {e}")
                break

def main():
    chat = OllamaChat()
    chat.interactive_chat()

if __name__ == '__main__':
    main()