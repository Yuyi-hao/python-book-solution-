from tkinter import * 
class MovingCircle:
    def __init__(self):
        window = Tk()
        window.title("Moving Circle")
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window,height = self.height,width = self.width,bg = "#ffffff")
        self.x = self.width/2
        self.y = self.height/2
        self.canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,tags = "circle")
        self.canvas.bind("<Right>",self.moveRight)
        self.canvas.bind("<Left>",self.moveLeft)
        self.canvas.bind("<Up>",self.moveUp)
        self.canvas.bind("<Down>",self.moveDown)
        self.canvas.focus_set()

        self.canvas.pack()
        window.mainloop()
    def moveRight(self,event):
        if self.x<self.width-10:
            self.x += 5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,tags = "circle")
    def moveLeft(self,event):
        if self.x > 10:
            self.x -= 5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,tags = "circle")
    def moveDown(self,event):
        if self.y < self.height-10:
            self.y += 5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,tags = "circle")
    def moveUp(self,event):
        if self.y > 10:
            self.y -= 5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,tags = "circle")


MovingCircle()