from tkinter import * 
class TwoCircles:
    def __init__(self):
        window = Tk()
        window.title("Two Circles")
        self.canvas = Canvas(window,height=750,width=750,bg="white")
        self.x1 = 20
        self.y1 = 20
        self.x2 = 50
        self.y2 = 120
        self.d = ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5
        self.canvas.pack()
        self.canvas.create_text((self.x1+self.x2)/2,(self.y1+self.y2)/2,tags="text",text=self.d)
        self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,tags="line")
        self.canvas.create_oval(self.x1-20,self.y1-20,self.x1+20,self.y1+20,tags="circle1",fill="red")

        self.canvas.create_oval(self.x2-20,self.y2-20,self.x2+20,self.y2+20,tags="circle1",fill="red")
        self.canvas.bind("<B1-Motion>",self.drawshape)
        window.mainloop()
    def drawshape(self,event):
        self.d = ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5
        
        self.canvas.delete("line")
        self.canvas.delete("circle1")
        self.canvas.delete("circle2")
        self.canvas.delete("line")
        self.canvas.delete("text")
        self.d1 = ((self.x1-event.x)**2 + (self.y1-event.y)**2)**0.5
        self.d2 = ((self.x2-event.x)**2 + (self.y2-event.y)**2)**0.5


        
        if self.d1 < 20:
            if (((event.x-self.x2)**2+(event.y-self.y2)**2)**0.5) > 70:
                self.x1 = event.x
                self.y1 = event.y
        if self.d2 < 20:
            if (((event.x-self.x1)**2+(event.y-self.y1)**2)**0.5) > 70:
                self.x2 = event.x
                self.y2 = event.y

            
        self.canvas.create_text((self.x1+self.x2)/2,(self.y1+self.y2)/2,tags="text",text=self.d)
        self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,tags="line")
        self.canvas.create_oval(self.x1-20,self.y1-20,self.x1+20,self.y1+20,tags="circle1",fill="red")

        self.canvas.create_oval(self.x2-20,self.y2-20,self.x2+20,self.y2+20,tags="circle1",fill="red")


TwoCircles()