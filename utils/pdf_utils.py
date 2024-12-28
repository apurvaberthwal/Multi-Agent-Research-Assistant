from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = "".join(page.extract_text() for page in reader.pages)
    return text
