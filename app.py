from models.ollama_chat import OllamaChat
import logging
import os

# Configuration du logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# Désactiver les logs httpx
# logging.getLogger("httpx").setLevel(logging.WARNING)

def main():
    temperature = float(os.getenv("TEMPERATURE", 0.2))
    chat = OllamaChat(system_prompt='Tu es un assistant français sympathique et intelligent. Réponds de manière naturelle et concise.', temperature=temperature)
    chat.interactive_chat()

if __name__ == '__main__':
    main()