from tkinter import * 
class ArrowLine:
    def __init__(self):
        window = Tk()
        window.title("Arrow Keys")
        height = 500
        width = 500
        self.canvas = Canvas(window,height=height,width=width)
        self.canvas.pack()
        self.canvas.bind("<Left>",self.drawLeft)
        self.canvas.bind("<Right>",self.drawRight)
        self.canvas.bind("<Up>",self.drawUp)
        self.canvas.bind("<Down>",self.drawDown)
        self.canvas.focus_set()
        self.x = width/2
        self.y = height/2

        window.mainloop()
    def drawLeft(self,event):
        self.canvas.create_line(self.x,self.y,self.x-5,self.y)
        self.x -= 5
    def drawRight(self,event):
        self.canvas.create_line(self.x,self.y,self.x+5,self.y)
        self.x += 5
    def drawUp(self,event):
        self.canvas.create_line(self.x,self.y,self.x,self.y-5)
        self.y -=5
    def drawDown(self,event):
        self.canvas.create_line(self.x,self.y,self.x,self.y+5)
        self.y += 5

ArrowLine()