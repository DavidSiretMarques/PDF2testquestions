from google import genai
from pypdf import PdfReader
with open("API_KEY.txt") as f:
    api_key= f.read()

client = genai.Client(api_key=api_key)
"""
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
"""
reader = PdfReader("example2.pdf")
source_content = ""
for page in reader.pages:
    source_content += page.extract_text() + "\n"
    

reader = PdfReader("example_test2.pdf")
example_content = ""
for page in reader.pages:
    example_content += page.extract_text() + "\n"
    
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Using the following content as reference, create a test with 5 questions and answers. Leave the answers and reference at the end of the test\n\nReference Content:\n{}\n\nExample Test Format:\n{}\n\nCreate the test now.".format(source_content, example_content))

print(response.text)