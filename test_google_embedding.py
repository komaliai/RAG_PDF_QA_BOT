from google import genai

# 🔑 Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)

try:
    response = client.models.embed_content(
        model="models/text-embedding-004",
        contents="Hello world"
    )

    print("✅ SUCCESS: Embedding works!")
    print("Vector length:", len(response.embeddings[0].values))

except Exception as e:
    print("❌ ERROR OCCURRED:")
    print(e)