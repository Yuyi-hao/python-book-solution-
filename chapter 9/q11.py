from datetime import datetime
from tkinter import *
import math 
class Clock:
    def __init__(self):
        window = Tk()
        window.title("Clock")
        self.canvas = Canvas(window,height = 500,width = 500,bg = "#474444")
        self.canvas.pack()
        #frame
        self.canvas.create_oval(100,50,400,350)
        
        self.x,self.y = 250,200
        self.secondHand = 120
        self.minuteHand = 110
        self.hourHand = 100
        self.textAlign = 140
        #digits
        for i in range(1,13):
            self.canvas.create_text(self.x+self.textAlign*math.cos(math.pi*(3-i)/6),self.y-self.textAlign*math.sin(math.pi*(3-i)/6),text=f'{i}')

        #time 
        self.now = datetime.now().strftime("%H:%M:%S")
        self.nowHour = (math.pi/2 - (math.pi/6*(datetime.now().hour%12+(datetime.now().minute/60))))
        self.nowMinute = math.pi/2 - ((datetime.now().minute + (datetime.now().second/60))*math.pi)/30
        self.nowSeconds = math.pi/2 - (datetime.now().second*math.pi)/30

        self.secondHandNeedle = self.canvas.create_line(self.x,self.y,self.x+self.secondHand*math.cos(self.nowSeconds),self.y-self.secondHand*math.sin(self.nowSeconds),width=1,fill="#A61717",arrow="last")
        self.minuteHandNeedle = self.canvas.create_line(self.x,self.y,self.x+self.minuteHand*math.cos(self.nowMinute),self.y-self.minuteHand*math.sin(self.nowMinute),width=3,fill="#0c136e",arrow="last")
        self.hourHandNeedle = self.canvas.create_line(self.x,self.y,self.x+self.hourHand*math.cos(self.nowHour),self.y-self.hourHand*math.sin(self.nowHour),width=5,fill="black",arrow="last")
        
        self.textTime = self.canvas.create_text(250,370,text=self.now)
        
         #hands
        def drawHands():
            self.canvas.delete(self.hourHandNeedle)
            self.canvas.delete(self.minuteHandNeedle)
            self.canvas.delete(self.secondHandNeedle)
            self.canvas.delete(self.textTime)
            self.now = datetime.now().strftime("%H:%M:%S")
            self.nowHour = (math.pi/2 - (math.pi/6*(datetime.now().hour%12+(datetime.now().minute/60))))
            self.nowMinute = math.pi/2 - ((datetime.now().minute + (datetime.now().second/60))*math.pi)/30
            self.nowSeconds = math.pi/2 - (datetime.now().second*math.pi)/30
            
            self.hourHandNeedle = self.canvas.create_line(self.x,self.y,self.x+self.hourHand*math.cos(self.nowHour),self.y-self.hourHand*math.sin(self.nowHour),width=5,fill="black",arrow="last")
            self.minuteHandNeedle = self.canvas.create_line(self.x,self.y,self.x+self.minuteHand*math.cos(self.nowMinute),self.y-self.minuteHand*math.sin(self.nowMinute),width=3,fill="#0c136e",arrow="last")
            self.secondHandNeedle = self.canvas.create_line(self.x,self.y,self.x+self.secondHand*math.cos(self.nowSeconds),self.y-self.secondHand*math.sin(self.nowSeconds),width=1,fill="#A61717",arrow="last")
            
            self.textTime = self.canvas.create_text(250,370,text=self.now)
            self.canvas.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill="black")
            self.canvas.after(10,drawHands)

             
        drawHands() 

        window.mainloop()
Clock()
