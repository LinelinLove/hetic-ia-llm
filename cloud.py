import os
import requests
from dotenv import load_dotenv

load_dotenv()

def download_file(file_id, api_key, destination_path):
    """
    Télécharge un fichier Google Drive en utilisant l'API et une clé API.
    """
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={api_key}"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(destination_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Fichier téléchargé avec succès : {destination_path}")
    else:
        print(f"Échec du téléchargement : {response.status_code} - {response.text}")


file_id = os.getenv("FILE_ID")
api_key = os.getenv("API_KEY")
destination_path = "./pdf/temp.pdf"

download_file(file_id, api_key, destination_path)
