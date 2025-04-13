import fitz # PyMuPDF
import re
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
import numpy as np

def pdf_to_words(pdf_path):
    words = []
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text = page.get_text()
            words.extend(re.findall(r'\b\w+\b', text))
    return words

pdf_path = './sample_data/javascript_tutorial.pdf'
words = pdf_to_words(pdf_path)

wordIndexToPrint = 10

tokenized_words = [word_tokenize(word.lower()) for word in words]

print(tokenized_words)

print("Extracted word to print:", words[wordIndexToPrint])

model = Word2Vec(sentences=tokenized_words, vector_size=100, window=5, min_count=1, workers=4)

word_embedding = model.wv[wordIndexToPrint]

embedding_string = np.array2string(word_embedding, separator=',', precision=6, suppress_small=True)

print("Word Embedding to print:", embedding_string)