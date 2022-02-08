from tkinter import *
from turtle import bgcolor 
class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("Radio buttons and buttons")
        self.x = 100
        self.y = 50
        self.width = 200
        self.height = 100
        self.color = StringVar(value="Red")
        self.frame1 = Frame(window)
        self.frame1.pack()
        self.frame2 = Frame(window)
        self.frame2.pack()
        self.frame3 = Frame(window)
        self.frame3.pack()
        self.canvas = Canvas(self.frame2,height = self.height,width = self.width,bg = "#9b82ff")
        self.canvas.pack()
        self.canvas.create_text(self.x,self.y,text="welcome",tags = "text",fill=self.color.get())
        Radiobutton(self.frame1,text="Red",variable=self.color,command=self.colorChange,value="Red").pack(side="left")
        Radiobutton(self.frame1,text="Yellow",variable=self.color,command=self.colorChange,value="Yellow").pack(side="left")
        Radiobutton(self.frame1,text="White",variable=self.color,command=self.colorChange,value="White").pack(side="left")
        Radiobutton(self.frame1,text="Gray",variable=self.color,command=self.colorChange,value="Gray").pack(side="left")
        Radiobutton(self.frame1,text="Green",variable=self.color,command=self.colorChange,value="Green").pack(side="left")
        Button(self.frame3,text="<=",command=self.moveLeft).pack(side="left")
        Button(self.frame3,text="=>",command=self.moveRight).pack(side="left")

        window.mainloop()
    def moveRight(self):
        self.canvas.delete("text")
        if self.x < 170:
            self.x += 5
        self.canvas.create_text(self.x,self.y,text="welcome",tags = "text",fill=self.color.get())
    def moveLeft(self):
        self.canvas.delete("text")
        if self.x >25:
            self.x -= 5
        self.canvas.create_text(self.x,self.y,text="welcome",tags = "text",fill=self.color.get())
    def colorChange(self):
        self.canvas.delete("text")
        self.canvas.create_text(self.x,self.y,text="welcome",tags = "text",fill=self.color.get())
        


MainGUI()