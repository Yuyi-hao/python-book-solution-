from tkinter import *
class Rectanguloid:
    def __init__(self):
        window = Tk()
        window.title("Rectanguloid")
        self.canvas = Canvas(window,width=500,height=500,bg="white")
        self.canvas.pack()
        self.x = 250
        self.y = 250

        self.canvas.create_rectangle(self.x-50,self.y-40,self.x+50,self.y+40)
        self.canvas.create_rectangle(self.x-30,self.y-20,self.x+70,self.y+60)

        self.canvas.create_line(self.x-50,self.y-40,self.x-30,self.y-20)
        self.canvas.create_line(self.x-50,self.y+40,self.x-30,self.y+60)
        self.canvas.create_line(self.x+50,self.y-40,self.x+70,self.y-20)
        self.canvas.create_line(self.x+50,self.y+40,self.x+70,self.y+60)
        window.mainloop()

Rectanguloid()
