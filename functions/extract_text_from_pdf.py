import PyPDF2

# Fonction pour extraire le texte du fichier PDF
def extract_text_from_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text