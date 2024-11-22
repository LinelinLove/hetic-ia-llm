from Classes.OllamaChat import OllamaChat
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)

def main():
    chat = OllamaChat(system_prompt='Tu es un assistant français sympathique et intelligent. Réponds de manière naturelle et concise.')
    chat.interactive_chat()

if __name__ == '__main__':
    main()