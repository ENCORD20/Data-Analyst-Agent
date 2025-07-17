import pandas as pd
import pdfplumber
import pytesseract
from PIL import Image
from docx import Document

def extract_from_txt(file):
    return file.read().decode("utf-8")

def extract_from_csv(file):
    return pd.read_csv(file)

def extract_from_excel(file):
    return pd.read_excel(file)

def extract_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def extract_from_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_from_image(file):
    return pytesseract.image_to_string(Image.open(file))

def get_text_or_df(file, filetype):
    if filetype == "txt":
        return extract_from_txt(file)
    elif filetype == "csv":
        return extract_from_csv(file)
    elif filetype == "xlsx":
        return extract_from_excel(file)
    elif filetype == "pdf":
        return extract_from_pdf(file)
    elif filetype == "docx":
        return extract_from_docx(file)
    elif filetype in ["png", "jpg", "jpeg"]:
        return extract_from_image(file)
    else:
        raise ValueError("Unsupported file type")
