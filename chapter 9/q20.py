from tkinter import * 
class InsideCircle:
    def __init__(self):
        window = Tk()
        window.title("Inside the circle?")
        self.canvas = Canvas(window,height=500,width=500,bg="#ffffff")
        self.canvas.pack()
        self.canvas.create_oval(50,10,150,110,tags="circle")
        self.canvas.bind("<B1-Motion>",self.showText)
        self.canvas.bind("<ButtonRelease-1>",self.cleartext)
        window.mainloop()
    def showText(self,event):
        d = ((event.x-100)**2 + (event.y-60)**2)**0.5
        self.canvas.delete("text")
        string = f'Mouse pointer is {"in" if d<50 else "not in"} the circle'
        self.canvas.create_text(event.x,event.y,text=string,tags="text")
    def cleartext(self,event):
        self.canvas.delete("text")
InsideCircle()