import tkinter as tk
import tkinter.ttk as ttk
import re

window = tk.Tk() # Window configurations
window.title("FFTCG card finder")
window.configure(bg='black')

setAnswer = tk.StringVar()

# Functions
def clear():
    setAnswer.set("")

def cardSearchCode():
    cardToFind = setAnswer.get()
    cardNameRegex = re.match('^\d{1,2}-\d{3}[CRHLS]+$', cardToFind)
    print(cardNameRegex)
    print(cardToFind)

def cardSearchName():
    pass
        
# Initialize widgets
label = tk.Label(window, text= "Welcome to the FFTCG spreadsheet searcher!\n\nNote: This spreadsheet doesn't contain cards from opus 7 or 14 because all of the Commons and Rares were obtained from these sets.\n\nEnter something then click one of the buttons to begin.\n\n")
codeInput = tk.Entry(window, width=25, textvariable=setAnswer)
cardInput = tk.Entry(window, width=25, textvariable=setAnswer)
cardCodeButton = tk.Button(window, text="Code", command=cardSearchCode)
cardNameButton = tk.Button(window, text="Card Name", command=cardSearchName)
ClearButton = tk.Button(window, text="Clear", command=clear)

# Placing widgets on window
label.grid(row=0,column=1,padx=50 , pady=50)
ClearButton.grid(row=3,column=0)
codeInput.grid(row=1, column=1)
cardInput.grid(row=1, column=2)
cardCodeButton.grid(row=3, column=1)
cardNameButton.grid(row=3, column=2)


window.mainloop()