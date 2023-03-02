import tkinter as tk
import tkinter.ttk as ttk
from CellFormulas import find_cardLocation
from path import File, SheetNames

window = tk.Tk() # Window configurations
window.title("FFTCG card finder")
window.configure(bg='black')

setCodeAnswer = tk.StringVar()
setNameAnswer = tk.StringVar()

# Functions
def clear():
    setCodeAnswer.set("")
    setNameAnswer.set("")

def cardSearchCode():
    cardToFind = setCodeAnswer.get().upper()
    output.delete(0.0, tk.END)
    for sheet in SheetNames:
        currentSheet = File[sheet]
        output.insert(tk.END, f"{currentSheet}\n")
        output.insert(tk.END, f"{str(find_cardLocation(currentSheet, cardToFind))}\n")

def cardSearchName():
    cardToFind = setNameAnswer.get().upper()
    output.delete(0.0, tk.END)
    for sheet in SheetNames:
        currentSheet = File[sheet]
        output.insert(tk.END, f"{currentSheet}\n")
        output.insert(tk.END, f"{str(find_cardLocation(currentSheet, cardToFind))}\n")
        
# Initialize widgets
label = tk.Label(window, text= "Welcome to the FFTCG spreadsheet searcher!\n\nNote: This spreadsheet doesn't contain cards from opus 7 or 14 because all of the Commons and Rares were obtained from these sets.\n\nEnter something then click one of the buttons to begin.\n\n")
codeInput = tk.Entry(window, width=25, textvariable=setCodeAnswer)
nameInput = tk.Entry(window, width=25, textvariable=setNameAnswer)
outputLabel = tk.Label(window, text="The card is at:")
output = tk.Text(window, width=100, height=35, bg="white", wrap="word")
cardCodeButton = tk.Button(window, text="Code", command=cardSearchCode)
cardNameButton = tk.Button(window, text="Card Name", command=cardSearchName)
ClearButton = tk.Button(window, text="Clear", command=clear)

# Placing widgets on window
label.grid(row=0,column=1,padx=50 , pady=50)
ClearButton.grid(row=2,column=0)
codeInput.grid(row=1, column=1)
nameInput.grid(row=1, column=2)
outputLabel.grid(row=3,column=1, pady=20)
output.grid(row=4,column=1, columnspan=10)
cardCodeButton.grid(row=2, column=1)
cardNameButton.grid(row=2, column=2)


window.mainloop()