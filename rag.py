from models.ollama_chat import OllamaChat
from functions.extract_text_from_pdf import extract_text_from_pdf
from functions.download_file import download_file
import os
from dotenv import load_dotenv
import logging

# Configuration du logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logging.getLogger("httpx").setLevel(logging.WARNING)

load_dotenv()

def main():

    file_id = os.getenv("FILE_ID")
    api_key = os.getenv("CLOUD_API_KEY")
    file_path = './pdf/temp.pdf'

    if not file_id or not api_key:
        print("Les variables d'environnement FILE_ID et CLOUD_API_KEY n'ont pas été définies.")
        print("Le fichier par défaut sera un conte sur 'Le Corbeau et le Renard'.")
        try:
            extracted_text = extract_text_from_pdf(file_path)
        except Exception as e:
            print(f"Erreur lors de l'extraction du texte : {e}")
            return
    else :
        try:
            download_file(file_id, api_key, file_path)
            extracted_text = extract_text_from_pdf(file_path)
        except Exception as e:
            print(f"Erreur lors du téléchargement ou de l'extraction du fichier : {e}")
            return
    
    temperature = float(os.getenv("TEMPERATURE", 0.2))
    chat = OllamaChat(system_prompt='Tu es un assistant intelligent. Tu réponds aux questions en fonction du contexte fourni de manière courte et concise.', temperature=temperature)
    chat.add_user_message(f"Voici le contenu du document que vous devez analyser : {extracted_text}")
    chat.interactive_chat()

if __name__ == '__main__':
    main()