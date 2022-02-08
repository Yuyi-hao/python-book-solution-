from tkinter import * 
class MovingCar:
    def __init__(self):
        window = Tk()
        window.title("Racing Car")
        self.width = 1000
        self.height = 200
        self.canvas = Canvas(window,height=self.height,width=self.width,bg="#ffffff")
        self.canvas.pack()
        self.x = 10
        self.y = 30
        self.speed = 5
        while True:
            self.x += self.speed
            self.drawCar()
            self.canvas.after(100) 
            self.canvas.update()
            if self.x >= self.width-60:
                self.x = 10
            self.canvas.bind("<Up>",self.increase)
            self.canvas.bind("<Down>",self.decrease)
            self.canvas.focus_set()
        window.mainloop()
    def drawCar(self):
        self.canvas.delete("car")
        self.canvas.create_rectangle(self.x,self.y+20,self.x+50,self.y+30,fill="red",tags="car")
        self.canvas.create_oval(self.x+10,self.y+30,self.x+20,self.y+40,fill="grey",tags="car")
        self.canvas.create_oval(self.x+30,self.y+30,self.x+40,self.y+40,fill="grey",tags="car")
        self.canvas.create_polygon(self.x+10,self.y+20,self.x+20,self.y+10,self.x+30,self.y+10,self.x+40,self.y+20,fill="yellow",tags="car")
    def increase(self,event):
        if self.speed < 100:
            self.speed += 3
    def decrease(self,event):
        if self.speed > 5:
            self.speed -= 3
MovingCar()