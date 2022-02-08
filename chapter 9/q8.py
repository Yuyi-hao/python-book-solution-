from tkinter import *
class TrianglePattern:
    def __init__(self):
        window = Tk()
        window.title("Triangle Pattern")
        self.frame1 = Frame(window)
        self.frame1.pack()
        Label(self.frame1,text="Enter row : ").grid(row=0,column=0)
        self.row = StringVar()
        Entry(self.frame1,text="Enter row : ",justify=RIGHT,textvariable=self.row).grid(row=0,column=1)
        Button(self.frame1,text="Print",command=self.printPattern).grid(row=0,column=2)
        self.frame2 = Frame(window)
        self.frame2.pack()
        self.string = StringVar()
        self.label = Label(self.frame2,text="Your pattern")
        self.label.pack()
        
        window.mainloop()
    def printPattern(self):
        result = ''
        row = int(self.row.get())
        for i in range(1,row+1):
            for k in range(1,i+1):
                result += str(k)+' '
            result += "\n"
        self.string = result
        self.label["text"] = self.string

TrianglePattern()