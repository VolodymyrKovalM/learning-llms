import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="embeddings")

collection.add(
    documents=[
        "Apple",
        "Oranges",
        "King",
        "Queen",
    ],
    ids=["id1", "id2", "id3", "id4"]
)

results = collection.query(
    query_texts=["Male"],
    n_results=4
)

print(results)