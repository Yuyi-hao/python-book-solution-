from tkinter import *
class BarChart:
    def __init__(self):
        
        window = Tk()
        window.title("Bar Chart")
        self.canvas = Canvas(window,height=200,width=500)
        self.canvas.pack()
        self.canvas.create_line(10,130,500,130)
        self.drawRectangle(100,20,130,20,"red","Project--20%")
        self.drawRectangle(100,10,130,145,"blue","Quizzes--10%")
        self.drawRectangle(100,30,130,270,"green","Midterm--30%")
        self.drawRectangle(100,40,130,395,"orange","Final--40%")

        window.mainloop()
    def drawRectangle(self,width,height,base,startingPosition,color,text):
        height = height*2
        self.canvas.create_rectangle(startingPosition,base-height,startingPosition+width,base,fill=color)
        self.canvas.create_text(startingPosition+width/2,base-height-10,text=text)
BarChart()