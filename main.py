"""import pdftotext

# Load your PDF
with open("example.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
print(pdf[1])

# Read all the text into one string
print("\n\n".join(pdf))
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
