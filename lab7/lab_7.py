from openai import OpenAI
client = OpenAI(api_key="")

response = client.embeddings.create(
    input="The sun shines brightly in the sky",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)
