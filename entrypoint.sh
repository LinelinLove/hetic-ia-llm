#!/bin/bash
# Start Ollama service
ollama serve &

until curl --silent --fail http://localhost:11434; do
    echo "En attente du démarrage du serveur Ollama..."
    sleep 2
done
echo "Serveur Ollama prêt !"

ollama pull llama3.2

python app.py
