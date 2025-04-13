import fitz # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize
import re
from sentence_transformers import SentenceTransformer

nltk.download('punkt_tab')

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def split_into_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

pdf_path = './sample_data/javascript_tutorial.pdf'
text = extract_text_from_pdf(pdf_path)

sentences = split_into_sentences(text)

# Two different models to try
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

embeddings = model.encode(sentences)

# Print each sentence and its embeddings as arrays in string representation
for sentence, embedding in zip(sentences, embeddings):
    embedding_array_string = '[' + ','.join(map(str, embedding)) + ']'
    print(f"Sentence: {sentence}")
    print(f"Embedding: {embedding_array_string}")