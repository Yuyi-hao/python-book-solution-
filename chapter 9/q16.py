from tkinter import * 
class DisplayFan:
    def __init__(self):
        window = Tk()
        window.title("Fan")
        self.initial = 0
        self.canvas = Canvas(window,height= 500,width= 500,bg="#ffffff")
        self.canvas.pack()
        while True:
            self.initial += 5
            self.drawFan(self.initial)
            self.canvas.after(100) 
            self.canvas.update()
        window.mainloop()
    
    def drawFan(self,initial):
        self.canvas.delete("fan")
        for i in range(1,5):
                self.Drawfan = self.canvas.create_arc(100,100,400,400,start=initial,extent=30,fill="grey",tags="fan")
                initial += i*90
        if initial == 360:
            initial = 0
        else:
            initial +=10
    

DisplayFan()