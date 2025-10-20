
from google import genai
with open("API_KEY.txt") as f:
    api_key= f.read()
    print(api_key)
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)