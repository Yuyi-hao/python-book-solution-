from tkinter import * 
import random
def toHexChar(n):
    if n <= 9 and n >= 0:
        return chr(n + ord('0'))
    else: 
        return chr(n - 10 + ord('A'))
class RandomBalls:
    def __init__(self):
        window = Tk()
        window.title("Random Balls")
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window,height=self.height,width = self.width,bg="white")
        self.canvas.pack()
        self.display()
        Button(window,text="Display",command=self.display).pack()
        window.mainloop()
    def display(self):
        self.canvas.delete("dots")
        for i in range(10):
            self.color = "#"
            for j in range(6):
                self.c = toHexChar(random.randint(0,15))
                self.color += self.c
            self.x = random.randint(0,self.width-10)
            self.y = random.randint(0,self.height-10)
            self.canvas.create_oval(self.x,self.y,self.x+10,self.y+10,tags="dots",fill=self.color)

RandomBalls()