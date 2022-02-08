from tkinter import * 
class IntersectingPoint:
    def __init__(self):
        window = Tk()
        window.title("Intersecting point")
        self.canvas = Canvas(window,width = 500,height = 500,bg = "white")
        self.canvas.pack()
        self.x1 = 20
        self.y1 = 20
        self.x2 = 56
        self.y2 = 130
        self.x3 = 100
        self.y3 = 20
        self.x4 = 16
        self.y4 = 130
        a1 = self.y1-self.y2
        b1 = self.x2-self.x1
        c1 = (self.y1-self.y2)*self.x1 - (self.x1-self.x2)*self.y1
        a2 = self.y3-self.y4
        b2 = self.x4-self.x3
        c2 = (self.y3-self.y4)*self.x3 - (self.x3-self.x4)*self.y3


        x = ((b2*c1) - (b1*c2))/((a1*b2) - (b1*a2))
        y = ((a1*c2) - (c1*a2))/((a1*b2) - (b1*a2))
        self.canvas.create_oval(x-5,y-5,x+5,y+5,tags="point",fill="red")

        self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,tags="line1")
        self.canvas.create_line(self.x3,self.y3,self.x4,self.y4,tags="line2")
        self.canvas.bind("<B1-Motion>",self.movingPoints)

        window.mainloop()

    def movingPoints(self,event):
        self.canvas.delete("line1")
        self.canvas.delete("line2")
        self.canvas.delete("point")

        self.d1 = ((event.x-self.x1)**2+(event.y-self.y1)**2)**0.5
        self.d2 = ((event.x-self.x2)**2+(event.y-self.y2)**2)**0.5
        self.d3 = ((event.x-self.x3)**2+(event.y-self.y3)**2)**0.5
        self.d4 = ((event.x-self.x4)**2+(event.y-self.y4)**2)**0.5

        if self.d1 < 5:
            self.canvas.delete("line1")
            self.x1 = event.x
            self.y1 = event.y
        elif self.d2 < 5:
            self.canvas.delete("line1")
            self.x2 = event.x
            self.y2 = event.y
        elif self.d3 < 5:
            self.canvas.delete("line2")
            self.x3 = event.x
            self.y3 = event.y
        elif self.d4 < 5:
            self.canvas.delete("line2")
            self.x4 = event.x
            self.y4 = event.y
        
        a1 = self.y1-self.y2
        b1 = self.x2-self.x1
        c1 = (self.y1-self.y2)*self.x1 - (self.x1-self.x2)*self.y1
        a2 = self.y3-self.y4
        b2 = self.x4-self.x3
        c2 = (self.y3-self.y4)*self.x3 - (self.x3-self.x4)*self.y3


        x = ((b2*c1) - (b1*c2))/((a1*b2) - (b1*a2))
        y = ((a1*c2) - (c1*a2))/((a1*b2) - (b1*a2))

        
        self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,tags="line1")
        self.canvas.create_line(self.x3,self.y3,self.x4,self.y4,tags="line1")

        self.canvas.create_oval(x-5,y-5,x+5,y+5,tags="point",fill="red")
IntersectingPoint()





