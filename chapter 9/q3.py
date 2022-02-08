from tkinter import *
class DrawFigure:
    def __init__(self):
        window = Tk()
        window.title("Radiobuttons and Checkbuttons")
        self.width = 400
        self.height = 200
        self.canvas = Canvas(window,width=self.width,height=self.height,bg="white")
        self.canvas.pack()
        self.frame1 = Frame(window)
        self.frame1.pack()
        self.shape = StringVar(value="R")
        self.isFill = IntVar(value=0)
        self.drawShape()
        Radiobutton(self.frame1,text = "Rectangle",variable=self.shape,value="R",command=self.drawShape).pack()
        Radiobutton(self.frame1,text = "Oval",variable=self.shape,value="O",command=self.drawShape).pack()

        Checkbutton(self.frame1,text = "Filled",variable=self.isFill,command=self.drawShape).pack()

        window.mainloop()
    def drawShape(self):
        self.canvas.delete("shape")
        if self.shape.get() == "R":
            self.canvas.create_rectangle(self.width/2-50,self.height/2-40,self.width/2+50,self.height/2+40,tags="shape")
        elif self.shape.get() == "O":
            self.canvas.create_oval(self.width/2-50,self.height/2-40,self.width/2+50,self.height/2+40,tags="shape")
        if self.isFill.get():
            self.canvas.itemconfig("shape",fill="red")
        else:
            self.canvas.itemconfig("shape",fill="white")
    

DrawFigure()