# Import necessary libraries
import fitz # PyMuPDF
import re

def pdf_to_words(pdf_path):
    words = []
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text = page.get_text()
            words.extend(re.findall(r'\b\w+\b', text))
    return words


pdf_path = './sample_data/javascript_tutorial.pdf'
result = pdf_to_words(pdf_path)
print(result)
print(f"Total words extracted: {len(result)}")
