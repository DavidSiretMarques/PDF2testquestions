"""
Main program for the PDF2test app

"""

from pypdf import PdfReader

reader = PdfReader("example_test2.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
    print(text)

print(text)

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(text)
