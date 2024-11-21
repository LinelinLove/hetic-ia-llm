#!/bin/bash
# Start Ollama service
ollama serve &

# Attendez que le service Ollama soit prêt (en utilisant curl pour vérifier l'état du serveur)
until curl --silent --fail http://localhost:11434; do
    echo "En attente du démarrage du serveur Ollama..."
    sleep 2
done
echo "Serveur Ollama prêt !"

# Pull Llama3 model
ollama pull llama3.2

# Run Python application
python app.py
