""""
Para probar diferentes cosas antes de añadirlas al programa principal
"""

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
from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader

def read_pdf():
    filepath = filedialog.askopenfilename(
        initialdir="D:\\\MEGA\\Python\\Proyectos-varios-python\\PDF2test\\PDF2testquestions\\",
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if not filepath:
        return "Cancelled", None # User cancelled the file dialog

    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    # Change label contents
    label_file_explorer.configure(text="File Opened: {}.\n Contents :\n {}".format(filepath, text))
    return text, filepath

window = Tk()
# Set window title
window.title('File Explorer')
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            #width = 100, height = 4,
                            fg = "blue")
button_explore = Button(window,
                        text = "Browse Files",
                        command = read_pdf)
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
# Grid method is chosen for placing the widgets at respective positions in a table like structure by specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()

with open("{}.txt".format(filepath), "w", encoding='utf-8') as f:
    f.write(text)
