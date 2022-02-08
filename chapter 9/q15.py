from tkinter import * 
class DisplayFan:
    def __init__(self):
        window = Tk()
        window.title("Fan")
        self.canvas = Canvas(window,height= 500,width= 500,bg="#ffffff")
        self.canvas.pack()
        initial = 0
        for i in range(1,5):
            self.canvas.create_arc(100,100,400,400,start=initial,extent=30,fill="grey")
            initial += i*90

        window.mainloop()

DisplayFan()