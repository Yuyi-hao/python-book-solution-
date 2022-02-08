from calendar import day_abbr
from tkinter import * 
class DynamicCircles:
    def __init__(self):
        window = Tk()
        window.title("Dynamic Circles")
        self.width = 500
        self.height = 500
        self.x = self.width/2 
        self.y = self.height/2
        self.length = 10
        self.tag = 0
        self.canvas = Canvas(window,height=self.height,width=self.width,bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>",self.drawCircle)
        self.canvas.bind("<Button-3>",self.removeCircle)
        window.mainloop()
    def drawCircle(self,event):
        self.tag +=1
        self.canvas.create_oval(self.x-self.length,self.y-self.length,self.x+self.length,self.y+self.length,tags=str(self.tag))
        if self.length < self.width/2:
            self.length +=10
        print("drew",self.tag)

    def removeCircle(self,event):
        self.canvas.delete(str(self.tag))
        self.tag -= 1
        self.length -=10
        print("removed",self.tag)

DynamicCircles()