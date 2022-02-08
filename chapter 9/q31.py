from tkinter import *
class FiveCircles:
    def __init__(self):
        window = Tk()
        window.title("Dragging the blue circle")
        self.canvas= Canvas(window,height=500,width=500,bg="white")
        self.canvas.pack()
        self.x = 250
        self.y = 250
        self.bx = 180
        self.by = 250
        self.canvas.create_oval(self.bx-30,self.y-30,self.bx+30,self.by+30,tags="blue",fill="blue")
        self.canvas.create_oval(220,250-30,280,250+30,fill="green")
        self.canvas.create_oval(290,250-30,350,250+30,fill="yellow")
        self.canvas.create_oval(180,250,240,250+60,fill="red")
        self.canvas.create_oval(260,250,320,250+60,fill="orange")
        self.canvas.bind("<B1-Motion>",self.dragBlue)
        window.mainloop()
    def dragBlue(self,event):
        self.canvas.delete("blue")
        self.canvas.create_oval(event.x-30,event.y-30,event.x+30,event.y+30,tags="blue",fill="blue")
FiveCircles()
