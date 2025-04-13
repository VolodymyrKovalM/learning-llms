from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
import numpy as np

# Download the punkt tokenizer data
nltk.download('punkt')

words = [
    "apple",
    "banana",
    "cherry",
    "dog",
    "elephant",
    "forest",
    "guitar",
    "happiness",
    "island",
    "journey"
]

tokenized_words = [word_tokenize(sentence.lower()) for sentence in words]

print(tokenized_words)

model = Word2Vec(sentences=tokenized_words, vector_size=100, window=5, min_count=1, workers=4)

word_embedding = model.wv['island']

embedding_string = np.array2string(word_embedding, separator=',', precision=6, suppress_small=True)

print("Word Embedding:", embedding_string)