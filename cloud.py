from functions.download_file import download_file
import os
from dotenv import load_dotenv

load_dotenv()

file_id = os.getenv("FILE_ID")
api_key = os.getenv("CLOUD_API_KEY")
destination_path = "./pdf/temp.pdf"

download_file(file_id, api_key, destination_path)
