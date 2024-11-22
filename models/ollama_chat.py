import ollama
from typing import List, Dict

class OllamaChat:
    def __init__(self, model: str = 'llama3.2', system_prompt: str = 'Tu es un assistant intelligent.', temperature: float = 0.2):
        """
        Initialise une session de chat interactive avec Ollama
        """
        self.model = model
        self.client = ollama.Client(host='http://localhost:11434')
        self.conversation: List[Dict[str, str]] = [
            {
                'role': 'system', 
                'content': system_prompt
            }
        ]
        self.temperature = temperature

    def add_user_message(self, message: str):
        self.conversation.append({
            'role': 'user', 
            'content': message
        })

    def get_ai_response(self) -> str:
        try:
            response = self.client.chat(
                model=self.model, 
                messages=self.conversation,
                options={
                    'temperature': self.temperature  # Contrôle la créativité
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
        print("🤖 Assistant Ollama - Tapez 'exit', 'quit' ou 'bye' pour quitter")
        print(f"Temperature : {self.temperature}")
        print("-----------------------------------")

        while True:
            try:
                user_input = input("\n🧑 Vous : ")
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\n🤖 Au revoir !")
                    break
                
                self.add_user_message(user_input)
                
                print("\n🤖 Assistant : ", end='', flush=True)
                ai_response = self.get_ai_response()
                print(ai_response)

            except KeyboardInterrupt:
                print("\n\n🤖 Chat interrompu. Tapez 'exit' pour quitter.")
            except Exception as e:
                logger.error(f"Erreur durant le chat : {e}")
                break