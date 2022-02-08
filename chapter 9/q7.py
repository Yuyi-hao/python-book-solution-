from tkinter import *
class DrawGrid:
    def __init__(self) -> None:
        window = Tk()
        window.title("Grid")
        self.canvas = Canvas(window,width=160,height=160)
        self.canvas.pack()
        # Vertical line 
        for i in range(1,8):
            self.canvas.create_line(i*20,0,i*20,160)
        for j in range(1,8):
            self.canvas.create_line(0,j*20,160,j*20)

        window.mainloop()

DrawGrid()