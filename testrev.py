import tkinter as tk
from tkinter import ttk

# creating a class called PDFViewer
class TestSimu:
    # initializing the __init__ / special method
    def __init__(self, master):
        self.master=master

        #Setting title and icon of main window
        self.master.title('Revisión de preguntas')
        self.master.iconbitmap(self.master, 'working.ico')

        #setting window to center of the screen
        self.window_width = 580
        self.window_height = 520
        center_x = int(self.master.winfo_screenwidth()/2 - self.window_width / 2)
        center_y = int(self.master.winfo_screenheight()/2 - self.window_height / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        #Menu (WIP)
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        file_menu = tk.Menu(menu,tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        # add menu items to the File menu
        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...')#, command=self.open_file)
        file_menu.add_command(label='Close')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.master.destroy)
        # create the Help menu
        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')
        # add the Help menu to the menubar
        menu.add_cascade(label="Help", menu=help_menu)

        # layout on the root window
        self.master.rowconfigure(0, weight=4)
        self.master.rowconfigure(1, weight=1)
        
        #Creating Question and button frames
        question_frame = self.create_question_frame()
        question_frame.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E))
        button_frame = self.create_button_frame()
        button_frame.grid(column=0, row=1, sticky=(tk.S,tk.W,tk.E))
        
        self.master.grid_rowconfigure(0, weight=10)
        self.master.grid_rowconfigure(1, weight=1)
    
    #Create question frame
    def create_question_frame(self):
        
        frame = ttk.Frame(self.master)

        # Create Question and options
        selected_option=tk.StringVar()
        self.question = tk.Label(frame, bg='#FFFFFF', text=question['pregunta'], wraplength=self.window_width, justify='left',relief='solid', borderwidth=1)
        self.question.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E))
        self.options = ttk.Frame(frame)
        self.options.grid(column=0, row=1, sticky=(tk.N,tk.W,tk.E))
        self.options.opt1 = ttk.Radiobutton(self.options, text=question['opciones'][0],value=question['opciones'][0], variable=selected_option)
        self.options.opt1.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E))
        self.options.opt2 = ttk.Radiobutton(self.options, text=question['opciones'][1],value=question['opciones'][1], variable=selected_option)
        self.options.opt2.grid(column=0, row=1, sticky=(tk.N,tk.W,tk.E))
        self.options.grid(column=0, row=1, sticky=(tk.N,tk.W,tk.E))
        self.options.opt3 = ttk.Radiobutton(self.options, text=question['opciones'][2],value=question['opciones'][2], variable=selected_option)
        self.options.opt3.grid(column=0, row=2, sticky=(tk.N,tk.W,tk.E))
        self.options.opt4 = ttk.Radiobutton(self.options, text=question['opciones'][3],value=question['opciones'][3], variable=selected_option)
        self.options.opt4.grid(column=0, row=3, sticky=(tk.N,tk.W,tk.E))
        
        # Set weights for responsiveness (WIP   -- not working as intended)
        frame.rowconfigure(0, weight=10)
        frame.rowconfigure(1, weight=1)

        for widget in frame.winfo_children():
            widget.grid(padx=5, pady=5)

        return frame

    #Create button frame
    def create_button_frame(self):
        frame = ttk.Frame(self.master)

        frame.rowconfigure(0, weight=1)
        
        ttk.Button(frame, text='Anterior').grid(column=0, row=0)
        ttk.Button(frame, text='Siguient').grid(column=1, row=0)
        ttk.Button(frame, text='Corregir').grid(column=2, row=0)
        ttk.Button(frame, text='Finalizar').grid(column=3, row=0)
        ttk.Button(frame, text='Guardar pregunta').grid(column=4, row=0)
        ttk.Button(frame, text='Eliminar pregunta').grid(column=5, row=0)

        for widget in frame.winfo_children():
            widget.grid(padx=5, pady=5)

        return frame

if __name__ == "__main__":
    question = {
        "pregunta": "Según el Reglamento de Instalaciones de Protección Contra Incendios, ¿cuál es el objeto principal de este Reglamento?",
        "opciones": [
            "La regulación de la seguridad en túneles de carreteras del Estado.",
            "La determinación de las condiciones y requisitos exigibles al diseño, instalación, mantenimiento e inspección de los equipos y sistemas de protección activa contra incendios.",
            "El establecimiento de las normativas para la fabricación de extintores portátiles.",
            "La inspección de sistemas de protección pasiva contra incendios."
        ],
        "respuesta": "La determinación de las condiciones y requisitos exigibles al diseño, instalación, mantenimiento e inspección de los equipos y sistemas de protección activa contra incendios.",
        "tema": "Objeto del Reglamento",
        "dificultad": 1,
        "creation_date": "5/11/2025",
        "reference": "Artículo 1. Objeto y ámbito de aplicación material. 1. Constituye el objeto de este Reglamento la determinación de las condiciones y los requisitos exigibles al diseño, instalación/aplicación, mantenimiento e inspección de los equipos, sistemas y componentes que conforman las instalaciones de protección activa contra incendios."
    }
    root = tk.Tk()
    app = TestSimu(root)
    root.mainloop()
