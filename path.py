import openpyxl
import os
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter.filedialog import askopenfile

# Path = os.path.join(os.path.expanduser('~'), 'Documents', 'Spreadsheets', 'FFTCG_automated.xlsx')
# File = openpyxl.load_workbook(Path, data_only=True)
# SheetNames = File.sheetnames

# Create an instance of tkinter frame
win = tk.Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')], initialdir=os.path.join(os.path.expanduser('~'), 'Documents'))
    if file != None:
        filepath = os.path.abspath(file.name)
        ttk.Label(win, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()

# Add a Label widget
label = ttk.Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()