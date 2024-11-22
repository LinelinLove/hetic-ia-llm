# hetic-ia-llm

> Modèle : llama3.2 de Ollama

## Lancer le projet avec Docker

PS : Sur Windows ouvrir Docker Desktop au préalable

1. Cloner le projet : `git clone https://github.com/LinelinLove/hetic-ia-llm.git`

2. Aller dans le répertoire du projet : `cd hetic-ia-llm`

3. Build et lancer le conteneur : `docker-compose up -d --build`

4. Attendre que le chargement soit terminé jusqu'à qu'il a ces messages suivants (l'installation du modèle llama3.2 peut prendre du temps) :

> Regarder les logs avec : `docker-compose logs -f` ou directement sur docker-desktop

```
writing manifest
success
🤖 Assistant Ollama - Tapez 'exit' pour quitter
-----------------------------------
```

## 1. Sans RAG

> IA générative

Le projet est prêt à être lancé avec la commande suivante :

`docker-compose exec python-ollama python app.py`

Vous pouvez à présent donnere des prompts à l'IA !
(L'IA met du temps à répondre 20sec à 2min)

### Changer la température de l'IA

Vous pouvez également changer la température de l'IA (par défaut `TEMPERATURE=0.5`) :

> Privilégiez des valeurs entre 0.0 (+ rigide) et 1.0 (+ créatif) pour éviter des textes imprévisibles

`docker-compose exec -e TEMPERATURE=0.5 python-ollama python app.py`

## 2. Avec RAG

> IA générative avec extraction de texte (avec Google Cloud et Google Drive)

1. Sur `https://console.cloud.google.com/`, créer un projet puis : [Identifiants](https://console.cloud.google.com/apis/credentials)

2. `Créer des identifiants` puis copier la clé API

3. Puis dans [API et services](https://console.cloud.google.com/apis/dashboard), cliquer sur `Activer les API et les services`

4. Dans [Bibliothèque](https://console.cloud.google.com/apis/library), chercher et cliquer sur Google Drive API (dans Google workspace) et cliquer sur `Activer`

5. Renommer `.env.example` par `.env`et ajouter votre clé API

6. Dans votre Google Drive, importer un fichier PDF (plus le fichier est court, plus le traitement sera rapide) et générer un lien en public

7. Puis récupérer le `file_id` de votre fichier a partir du lien généré comme ci-dessous:

```
https://drive.google.com/file/d/file_id/view
```

et le coller dans le `.env` dans l'emplacement prévu

7. Lancer la commande : `docker-compose exec python-ollama python rag.py`

Votre fichier est installé depuis votre Google Drive

Vous pouvez à présent poser des questions sur le fichier PDF que vous avez fourni ! (L'IA peut mettre 2min à répondre)

> Si les valeurs `FILE_ID`et `CLOUD_API_KEY`du .env n'ont pas été défini, l'IA analysera le fichier qui est par défaut dans le dossier pdf

### 2ème méthode pour analyser un fichier

Vous pouvez préciser directement le `FILE_ID` et `CLOUD_API_KEY` dans la commande :

```
docker-compose exec -e FILE_ID=placeholder_for_file_id -e CLOUD_API_KEY=placeholder_for_cloud_api_key python-ollama python rag.py
```

> Si il y a déjà `FILE_ID` dans le fichier `.env`, le `FILE_ID` prise en compte sera celle de la commande, de même pour `CLOUD_API_KEY`

> Vous pouvez également mettre `CLOUD_API_KEY` dans le `.env` et juste modifier `FILE_ID` dans la commande

```
docker-compose exec -e FILE_ID=placeholder_for_file_id python-ollama python rag.py
```

Vous pouvez également changer la température en rajoute `-e TEMPERATURE=value`

```
docker-compose exec -e FILE_ID=placeholder_for_file_id -e CLOUD_API_KEY=placeholder_for_cloud_api_key -e TEMPERATURE=0.5 python-ollama python rag.py
```
