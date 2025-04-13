from sentence_transformers import SentenceTransformer

sentences = [
    "The sun shines brightly in the sky.",
    "She enjoys reading books on weekends.",
    "They walked along the quiet beach.",
    "My dog loves to play outside.",
    "He quickly finished his math homework.",
    "A beautiful rainbow appeared after rain.",
    "We traveled to the mountains last summer.",
    "Technology is changing the world rapidly.",
    "She baked a delicious chocolate cake today.",
    "He dreams of becoming an astronaut someday."
]

# Two different models to try
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

embeddings = model.encode(sentences)

# Print each sentence and its embeddings as arrays in string representation
for sentence, embedding in zip(sentences, embeddings):
    embedding_array_string = '[' + ','.join(map(str, embedding)) + ']'
    print(f"Sentence: {sentence}")
    print(f"Embedding: {embedding_array_string}")
    