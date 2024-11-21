# hetic-ia-llm

## Lancer le projet avec Docker

### Sans RAG

Cloner le projet : `git clone https://github.com/LinelinLove/hetic-ia-llm.git`

Aller dans le répertoire du projet : `cd hetic-ia-llm`

PS : Sur Windows ouvrir Docker Desktop au préalable
`docker-compose up -d --build`

Regarder les logs : `docker-compose logs -f` et attendre que le chargement soit terminé jusqu'à qu'il a ces messages suivants :

```
writing manifest
success
🤖 Assistant Ollama - Tapez 'exit' pour quitter
-----------------------------------
```

Le projet est prêt à être lancé :
`docker-compose exec python-ollama python app.py`

Vous pouvez à présent donnere des prompts à l'IA ! (L'assistant met du temps à répondre)

### Avec RAG avec Cloud
