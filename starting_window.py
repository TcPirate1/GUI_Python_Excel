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

def CardSearcher():
    cardToFind = setAnswer.get()
    cardNameRegex = re.match('^\d{1,2}-\d{3}[CRHLS]+$', cardToFind)
    if(cardNameRegex == None):
        print("This is not a match.")
    if(cardNameRegex != None):
        print("This is a match.")
        
# Initialize widgets
label = tk.Label(window, text= "Welcome to the FFTCG spreadsheet searcher!\n\nNote: This spreadsheet doesn't contain cards from opus 7 or 14 because all of the Commons and Rares were obtained from these sets.\n\nEnter something then click one of the buttons to begin.\n\n")
userInput = tk.Entry(window, width=25, textvariable=setAnswer)
cardCode = tk.Button(window, text="Code", command=CardSearcher)
cardName = tk.Button(window, text="Card Name", command=CardSearcher)
ClearButton = tk.Button(window, text="Clear", command=clear)

# Placing widgets on window
label.grid(row=0,column=1,padx=50 , pady=50)
userInput.grid(row=1, column=0, columnspan=3)
ClearButton.grid(row=2,column=0)
cardCode.grid(row=2, column=1)
cardName.grid(row=2, column=2)


window.mainloop()