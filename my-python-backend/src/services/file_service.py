from PyPDF2 import PdfFileReader

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfFileReader(file)
            text = ""
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"