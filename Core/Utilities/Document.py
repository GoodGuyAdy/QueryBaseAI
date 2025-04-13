import os
from docx import Document
from PyPDF2 import PdfReader


def extract_text_from_file(file):
    """
    Extract text from file object.
    """
    allowed_extensions = [".txt", ".md", ".docx", ".pdf"]
    filename = file.name
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    if ext not in allowed_extensions:
        raise ValueError(f"Unsupported file type: {filename}")

    try:
        if ext in [".txt", ".md"]:
            text = file.read().decode("utf-8")

        elif ext == ".docx":
            doc = Document(file)
            text = "\n".join([p.text for p in doc.paragraphs])

        elif ext == ".pdf":
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

        return text.strip()

    except Exception as e:
        raise ValueError(f"Error processing {filename}: {e}")
