import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os
# importing the PDFMiner class from the miner file
from pdfminer import PDFMiner

# creating a class called PDFViewer
class PDFViewer:
    # initializing the __init__ / special method
    def __init__(self, master):
        
        self.master=master
        # path for the pdf doc
        self.path = None
        # state of the pdf doc, open or closed
        self.fileisopen = None
        # author of the pdf doc
        self.author = None
        # name for the pdf doc
        self.name = None
        # the current page for the pdf
        self.current_page = 0
        # total number of pages for the pdf doc
        self.numPages = None
        
        #Setting title and icon of main window
        self.master.title('PDF Viewer')
        self.master.iconbitmap(self.master, 'pdf.ico')

        #setting window to center of the screen
        self.window_width = 580
        self.window_height = 520
        center_x = int(self.master.winfo_screenwidth()/2 - self.window_width / 2)
        center_y = int(self.master.winfo_screenheight()/2 - self.window_height / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        #Menu
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        file_menu = tk.Menu(menu,tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)

        # add menu items to the File menu
        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...', command=self.open_file)
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

        self.viewer_frame = self.create_viewer_frame()
        self.viewer_frame.grid(column=0, row=0)

        button_frame = self.create_button_frame()
        button_frame.grid(column=0, row=1)
    
    #Create viewer frame
    def create_viewer_frame(self):
        
        frame = ttk.Frame(self.master)

        # grid layout for the input frame
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(0, weight=3)

        # Create Canvas to view pdf
        self.output = tk.Canvas(frame, bg='#ECE8F3', width=560, height=435, highlightthickness=0)
        #Configuring the resize event for canvas (NOT WORKING PROPERLY YET)
        #self.output.bind("<Configure>", self.on_resize)
        #self.output.height = self.output.winfo_reqheight()
        #self.output.width = self.output.winfo_reqwidth()
        self.output.grid(column=0, row=0, sticky=tk.N)

        #create scrollbars and set them
        xscrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
        xscrollbar.grid(column=0, row=1, sticky=(tk.W, tk.E))
        yscrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        yscrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))
        self.output['xscrollcommand'] = xscrollbar.set
        self.output['yscrollcommand'] = yscrollbar.set
        xscrollbar.config(command=self.output.xview)
        yscrollbar.config(command=self.output.yview)
        self.page_label = ttk.Label(frame, text='page')
        self.page_label.grid(row=2, column=0, padx=5)

        for widget in frame.winfo_children():
            widget.grid(padx=5, pady=5)

        return frame

    #Function to resize canvas and its content (NOT WORKING PROPERLY YET)
    """
    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.output.width
        hscale = float(event.height)/self.output.height
        self.output.width = event.width
        self.output.height = event.height
        # resize the canvas 
        self.output.config(width=self.output.width, height=self.output.height)
        # rescale all the objects tagged with the "all" tag
        self.output.scale("all",0,0,wscale,hscale)
        print(f'Width: {self.output.width}, Height: {self.output.height},event width: {event.width}, event height: {event.height}')
    """
    #Create button frame
    def create_button_frame(self):
        frame = ttk.Frame(self.master)

        frame.rowconfigure(0, weight=1)
        
        self.uparrow_icon = tk.PhotoImage(file='arrowup.png')
        self.downarrow_icon = tk.PhotoImage(file='arrowdown.png')
        # resizing the icons to fit on buttons
        self.uparrow = self.uparrow_icon.subsample(1, 1)
        self.downarrow = self.downarrow_icon.subsample(1, 1)
        self.upbutton = ttk.Button(frame, image=self.uparrow, command=self.previous_page)
        self.upbutton.grid(row=0, column=1, padx=(250, 5), pady=8)
        self.downbutton = ttk.Button(frame, image=self.downarrow, command=self.next_page)
        self.downbutton.grid(row=0, column=2, pady=8)

        for widget in frame.winfo_children():
            widget.grid(padx=5, pady=5)

        return frame

    # function for opening pdf files
    def open_file(self):
        # open the file dialog
        filepath = fd.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(),
                                      filetypes=(('PDF', '*.pdf'), ))
        # checking if the file exists
        if filepath:
            # declaring the path
            self.path = filepath
            # extracting the pdf file from the path
            filename = os.path.basename(self.path)
            # passing the path to PDFMiner 
            self.miner = PDFMiner(self.path)
            # getting data and numPages
            data, numPages = self.miner.get_metadata()
            # setting the current page to 0
            self.current_page = 0
            # checking if numPages exists
            if numPages:
                # getting the title (If title is blank, setting it to Untitled)
                if data.get('title', filename[:-4]) == "":
                    self.name = "Untitled" 
                else:
                    self.name = data.get('title', filename[:-4])
                # getting the author
                self.author = data.get('author', None)
                self.numPages = numPages
                # setting fileopen to True
                self.fileisopen = True
                # calling the display_page() function
                self.display_page()
                # replacing the window title with the PDF document name
                self.master.title(self.name)

    # the function to display the page
    def display_page(self):
        # checking if numPages is less than current_page and if current_page is less than or equal to 0
        if 0 <= self.current_page < self.numPages:
            # getting the page using get_page() function from miner
            self.img_file = self.miner.get_page(self.current_page)
            # inserting the page image inside the Canvas
            self.output.create_image(0, 0, anchor='nw', image=self.img_file)
            # the variable to be stringified
            self.stringified_current_page = self.current_page + 1
            # updating the page label with number of pages 
            self.page_label['text'] = str(self.stringified_current_page) + ' of ' + str(self.numPages)
            # creating a region for inserting the page inside the Canvas
            region = self.output.bbox(tk.ALL)
            # making the region to be scrollable
            self.output.configure(scrollregion=region)
            
    # function for displaying next page
    def next_page(self):
        # checking if file is open
        if self.fileisopen:
            # checking if current_page is less than or equal to numPages-1
            if self.current_page <= self.numPages - 1:
                # updating the page with value 1
                self.current_page += 1
                # displaying the new page
                self.display_page()

    # function for displaying the previous page        
    def previous_page(self):
        # checking if fileisopen
        if self.fileisopen:
            # checking if current_page is greater than 0
            if self.current_page > 0:
                # decrementing the current_page by 1
                self.current_page -= 1
                # displaying the previous page
                self.display_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFViewer(root)
    root.mainloop()
