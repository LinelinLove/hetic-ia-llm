from models.ollama_chat import OllamaChat
from functions.extract_text_from_pdf import extract_text_from_pdf
import logging

# Configuration du logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logging.getLogger("httpx").setLevel(logging.WARNING)

def main():
    file_path = './pdf/temp.pdf'
    
    extracted_text = extract_text_from_pdf(file_path)
    chat = OllamaChat(system_prompt='Tu es un assistant intelligent. Tu réponds aux questions en fonction du contexte fourni de manière courte et concise.')
    chat.add_user_message(f"Voici le contenu du document que vous devez analyser : {extracted_text}")
    chat.interactive_chat()

if __name__ == '__main__':
    main()