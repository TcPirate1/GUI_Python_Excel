import openpyxl
import os
from tkinter import filedialog

# Path = os.path.join(os.path.expanduser('~'), 'Documents', 'Spreadsheets', 'FFTCG_automated.xlsx')
# File = openpyxl.load_workbook(Path, data_only=True)
# SheetNames = File.sheetnames

def select_file():
    Path = filedialog.askopenfile(mode='r', filetypes=[('Excel Files', '*.xlsx')], initialdir=os.path.join(os.path.expanduser('~'), 'Documents'))
    
    if Path and os.path.splitext(Path)[1] == '.xlsx':
        File = openpyxl.load_workbook(Path, data_only=True)
        SheetNames = File.sheetnames
        return File, SheetNames