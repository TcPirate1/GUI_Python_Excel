import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk() # Window configurations
window.title("FFTCG card finder")
window.configure(bg='black')

setAnswer = tk.StringVar()

# Initialize widgets
class HomeScreen:
    def __init__(self, window):
        self.screen()

# Functions
    def clear(self):
        setAnswer.set("")

    def search(self):
        # Destroying frame
        for widget in window.winfo_children():
            widget.destroy()

        self.frame = tk.Frame(window, width= 800, height= 800)
        label = tk.Label(window, text="Enter either a card code or name then click the respective button")
        userInput = tk.Entry(window, width=25, textvariable=setAnswer)
        cardCode = tk.Button(window, text="Code")
        cardName = tk.Button(window, text="Card Name")
        ClearButton = tk.Button(window, text="Clear", command=self.clear)

        label.grid(row=0,column=0, columnspan=3)
        userInput.grid(row=1, column=0, columnspan=3)
        ClearButton.grid(row=2,column=0)
        cardCode.grid(row=2, column=1)
        cardName.grid(row=2, column=2)

    def screen(self):
        self.frame = tk.Frame(window, width= 800, height= 800)
        self.label = tk.Label(window, text= "Welcome to the FFTCG spreadsheet searcher!\n\nNote: This spreadsheet doesn't contain cards from opus 7 or 14 because all of the Commons and Rares were obtained from these sets.\n\nClick one of the buttons to begin.\n\n").grid(row=0,column=1,padx=50 , pady=50)
        output = tk.Label(textvariable=setAnswer, width=25)
        Search = tk.Button(window, text="Search", command=self.search)
        # AddWorkSheet = tk.Button(window, text="Add worksheet")
        # WorkOnWorkSheet = tk.Button(window, text="Work on worksheet")
        # ViewWorkSheet = tk.Button(window, text="View empty cells in worksheet")
        # ChangeCellValue = tk.Button(window, text="Change cell value")

        # Placing widgets on window
        output.grid(row=1,column=1, columnspan=2)
        Search.grid(row=3,column=2)
        # AddWorkSheet.grid(row=3,column=3)
        # WorkOnWorkSheet.grid(row=3,column=4)
        # ViewWorkSheet.grid(row=3,column=5)
        # ChangeCellValue.grid(row=3,column=6)

HomeScreen(window)
window.mainloop()