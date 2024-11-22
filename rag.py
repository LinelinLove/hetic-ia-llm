from Classes.OllamaChat import OllamaChat
import PyPDF2
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Désactiver les logs httpx
logging.getLogger("httpx").setLevel(logging.WARNING)


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
    chat = OllamaChat(system_prompt='Tu es un assistant intelligent. Tu réponds aux questions en fonction du contexte fourni de manière courte et concise.')
    chat.add_user_message(f"Voici le contenu du document que vous devez analyser : {extracted_text}")
    chat.interactive_chat()

if __name__ == '__main__':
    main()