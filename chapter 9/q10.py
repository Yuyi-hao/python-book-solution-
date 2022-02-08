from tkinter import *
import math
class PiChart:
    def __init__(self):
        
        window = Tk()
        window.title("Pi Chart")
        self.canvas = Canvas(window,height=350,width=350)
        self.canvas.pack()
        self.width = 300
        self.height = 300
        self.radius = 100
        self.drawArc(0,72,"red","Project--20%")
        self.drawArc(72,36,"blue","Quizzes--10%")
        self.drawArc(36+72,108,"green","Midterm--30%")
        self.drawArc(108+73+36,144,"orange","Final--40%")
        window.mainloop()
    def drawArc(self,startPoint,extent,color,text):
        self.canvas.create_arc(self.width/2-self.radius,self.height/2-self.radius,self.width/2+self.radius,self.height/2+self.radius,start=startPoint,extent = extent,fill=color)

        x = self.width / 2 + self.radius * math.cos(math.radians(extent / 2 + startPoint))
        y = self.height / 2 - self.radius * math.sin(math.radians(extent / 2 + startPoint))

        self.canvas.create_text(x,y,text=text)
            
PiChart()