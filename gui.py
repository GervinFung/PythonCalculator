from tkinter import *
from tkinter import messagebox

class Calculator():
    def __init__(self, master):
        self.__master = master
        self.__equation = Entry(master, width = 47, borderwidth = 0)
        self.__equation.grid(row = 0, column = 0, columnspan = 10, padx = 10, pady = 10)
        master.title("PyCalculator")
        self.makeButton()

    def makeButton(self):
        numButtonList = []
        #NUMBER button
        for i in range(10):
            numButtonList.append(self.addButton(i))
        
        #OPERATION button
        addButton = self.addButton("+")
        subButton = self.addButton("-")
        mulButton = self.addButton("x")
        divButton = self.addButton("/")

        #CLEAR button
        clearButton = self.addButton("CLEAR")

        #EQUAL button
        equalButton = self.addButton("=")

        #ARRANGE each buttons into different rows
        row1 = [numButtonList[7], numButtonList[8], numButtonList[9], addButton]
        row2 = [numButtonList[4], numButtonList[5], numButtonList[6], subButton]
        row3 = [numButtonList[1], numButtonList[2], numButtonList[3], mulButton]
        row4 = [numButtonList[0], clearButton, equalButton, divButton]

        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for button in row:
                button.grid(row = r, column = c, columnspan = 1)
                c += 1
            r += 1

    #CREATE new button
    def addButton(self, value):
        return Button(self.__master, text = value, width = 9, background = "#48483E", command = lambda: self.buttonAction(str(value)))

    #MAKE buttion click work
    def buttonAction(self, value):
        currentEquation = str(self.__equation.get())
        if value == "CLEAR":
            self.__equation.delete(-1, END)

        elif value == "x":
            self.__equation.insert(0, currentEquation + "*")

        elif value == "=":
            #IF the equation is invalid catch the error
            try:
                #eval PARSE string as int and do calculation
                answer = str(eval(currentEquation))
                self.__equation.delete(-1, END)
                self.__equation.insert(0, answer)
            except:
                messagebox.showwarning("Warning", "Please enter proper mathematical equation")

        else:
            self.__equation.delete(0, END)
            self.__equation.insert(0, currentEquation + value)

def on_close():
    close = messagebox.askokcancel("Close", "Would you like to close the program?")
    if close:
        root.destroy()
if __name__ == "__main__":
    root = Tk()
    #SET gui location in center
    root.geometry("400x165+470+200")
    #SET background of calculator as black
    root.configure(background = "#272822")
    #GUI cannot resize
    root.resizable(False, False)
    calculator = Calculator(root)
    root.protocol("WM_DELETE_WINDOW",  on_close)
    root.mainloop()