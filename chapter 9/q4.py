from tkinter import *
class Drawrectangle:
    def __init__(self):
        window = Tk()
        window.title("Display Reactangle")
        
        self.canvas = Canvas(window,height=400,width=600)
        self.canvas.pack()
        
        for i in range(20):
            self.canvas.create_rectangle(10*i,10*i,600-i*10,400-i*10)
        window.mainloop()

Drawrectangle()