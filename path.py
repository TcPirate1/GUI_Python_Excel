import openpyxl
import os
from tkinter import filedialog

# Path = os.path.join(os.path.expanduser('~'), 'Documents', 'Spreadsheets', 'FFTCG_automated.xlsx')
# File = openpyxl.load_workbook(Path, data_only=True)
# SheetNames = File.sheetnames

def select_file():
    Path = filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')], initialdir=os.path.join(os.path.expanduser('~'), 'Documents'))
    
    if Path:
        File = openpyxl.load_workbook(Path, data_only=True)
        SheetNames = File.sheetnames
        return File, SheetNames