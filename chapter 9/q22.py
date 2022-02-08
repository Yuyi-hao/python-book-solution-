from tkinter import *  
import math

width = 200
height = 200
pendulumRadius = 150
ballRadius = 10
leftAngle = 120
rightAngle = 60


class MainGUI:
    def __init__(self):
        window = Tk()  
        window.title("Pendulum")  

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.angle = leftAngle  
        self.angleDelta = 1 
        self.delay = 100
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.speed)
        self.on = True
        while self.on:
            if self.on:
                self.canvas.delete("pendulum")
                self.displayPendulum()
                self.canvas.after(self.delay)
                self.canvas.update()

        window.mainloop()  

    def displayPendulum(self):
        x1 = width / 2
        y1 = 20

        if self.angle < rightAngle:
            self.angleDelta = 1  
        elif self.angle > leftAngle:
            self.angleDelta = -1  

        self.angle += self.angleDelta
        x = x1 + pendulumRadius * math.cos(math.radians(self.angle))
        y = y1 + pendulumRadius * math.sin(math.radians(self.angle))

        self.canvas.create_line(x1, y1, x, y, tags="pendulum")
        self.canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill="black", tags="pendulum")
        self.canvas.create_oval(x - ballRadius, y - ballRadius, x + ballRadius, y + ballRadius,
                                fill="black", tags="pendulum")

    def speed(self, event):
        if event.keysym == "Down":
            if self.delay < 200:
                self.delay += 10
        elif event.keysym == "Up":
            if self.delay > 10:
                self.delay -= 10
        elif event.keysym == "r":
            self.on = True
        elif event.keysym == "s": 
            self.on = False


MainGUI()