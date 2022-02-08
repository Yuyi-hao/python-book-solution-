from tkinter import *
class DisplayChessboard:
    def __init__(self):
        window = Tk()
        window.title("Display a Checkboard")
        self.canvas = Canvas(window,height = 200,width=200,bg="white")
        self.canvas.pack()
        self.draw()
        window.mainloop()
    def draw(self):
        x1=0
        y1=0
        m = -1
        k = 0
        for j in range(8):
            for i in range(4):
                x1 = 50*i+k*25
                y1 = j*25
                x2=x1+25
                y2=y1+25
                self.canvas.create_rectangle(x1,y1,x2,y2,fill="black")
            if m == 1:
                k = 0
            elif m == -1:
                k = 1
            m *= (-1)

DisplayChessboard()