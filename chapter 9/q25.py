from math import radians
from tkinter import * 
class TrafficLights:
    def __init__(self):
        window = Tk()
        window.title("Traffic Light")
        self.frame1 = Frame(window).pack()
        self.frame2 = Frame(window).pack()
        self.canvas = Canvas(window,height=400,width=400,bg="white")
        self.canvas.pack()
        self.color = StringVar(value="red")
        print(self.color)
        self.canvas.create_rectangle(170,110,240,310)
        self.canvas.create_oval(175,115,235,175,fill="red",tags="red")        
        self.canvas.create_oval(175,180,235,240,fill="white",tags="yellow")
        self.canvas.create_oval(175,245,235,305,fill="white",tags="green")

        Radiobutton(self.frame2,text="Red",variable=self.color,command=self.change,value="red").pack(side="left")
        Radiobutton(self.frame2,text="Yellow",variable=self.color,command=self.change,value="yellow").pack(side="left")
        Radiobutton(self.frame2,text="Green",variable=self.color,command=self.change,value="green").pack(side="left")
        print(self.color)

        window.mainloop()
    def change(self):
        self.canvas.itemconfig(self.color.get(),fill=self.color.get())
        if "red" not in self.color.get():
            self.canvas.itemconfig("red",fill="white")
        if "yellow" not in self.color.get():
            self.canvas.itemconfig("yellow",fill="white")
        if "green" not in self.color.get():
            self.canvas.itemconfig("green",fill="white")

TrafficLights()