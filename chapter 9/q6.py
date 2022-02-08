from tkinter import *
import random
class Tictactoeboard:
    def __init__(self):
        window = Tk()
        window.title("Tic-Tac-Toe")
        self.image1 = PhotoImage(file="ch9\\x.gif")
        self.image2 = PhotoImage(file="ch9\\o.gif")
        for i in range(3):
            for j in range(3):
                n = random.randint(0,1)
                if n==0:
                    Label(window,image=self.image1).grid(row=i,column=j)
                elif n ==1:
                    Label(window,image=self.image2).grid(row=i,column=j)

        window.mainloop()

Tictactoeboard()