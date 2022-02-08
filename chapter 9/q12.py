from tkinter import * 
class changeingMessage:
    def __init__(self):
        window = Tk()
        window.title("Rotating Message")
        self.text = StringVar()
        self.i = 0
        self.text = "Programming is fun"
        self.label = Label(window,text=self.text,height=10,width=50)
        self.label.pack()
        self.label.bind("<Button-1>",self.changeText)
        window.mainloop()

        
    def changeText(self,event):
        if self.i == 0:
            self.label["text"] = "Programming is fun"
            self.i = 1
        else:
            self.label["text"] = "It is fun to program"
            self.i = 0

        

changeingMessage()