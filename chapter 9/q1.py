from tkinter import * 
class Movingball:
    def __init__(self):
        window = Tk()
        window.title("Moving Ball")
        self.canvas = Canvas(window,height = 300,width=300,bg="white")
        self.canvas.pack()
        self.x = 150
        self.y = 150
        self.frame = Frame(window)
        self.frame.pack()
        Button(self.frame,text="Left",command=self.left).grid(row=0,column=0)
        Button(self.frame,text="Right",command=self.right).grid(row=0,column=1)
        Button(self.frame,text="Up",command=self.up).grid(row=0,column=2)
        Button(self.frame,text="Down",command=self.down).grid(row=0,column=3)
        self.canvas.create_oval(self.x-8,self.y-8,self.x+8,self.y+8,fill="red",tags="circle")
        window.mainloop()
    def left(self):
        if self.x > 10:
            self.x -=5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-8,self.y-8,self.x+8,self.y+8,fill="red",tags="circle")
    def right(self):
        if self.x < 290:
            self.x +=5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-8,self.y-8,self.x+8,self.y+8,fill="red",tags="circle")
    def up(self):
        if self.y > 10:
            self.y -=5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-8,self.y-8,self.x+8,self.y+8,fill="red",tags="circle")
    def down(self):
        if self.y < 290:
            self.y +=5
        self.canvas.delete("circle")
        self.canvas.create_oval(self.x-8,self.y-8,self.x+8,self.y+8,fill="red",tags="circle")

Movingball()