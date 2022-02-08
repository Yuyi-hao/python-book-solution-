from tkinter import * 
import random
class ArrowLine:
    def __init__(self):
        window = Tk()
        window.title("Randome an Arrow Line")
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window,height=self.height,width=self.width)
        self.canvas.pack()
        self.draw()
        Button(window,text="Draw a Random Arrow Line",command = self.draw).pack()
        window.mainloop()
    def draw(self):
        self.canvas.delete("line")
        self.canvas.create_line(random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),tags="line",arrow="last")

ArrowLine()