from tkinter import * 
class MousePosition:
    def __init__(self):
        window = Tk()
        window.title("Mouse Position")
        self.canvas = Canvas(window,height= 500, width = 500,border=2) 
        self.canvas.pack()
        self.text = self.canvas.create_text(0,0,text="")
        self.canvas.bind("<Button-1>",self.mousePosition)
        window.mainloop()
        
    def mousePosition(self,event):
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(event.x,event.y,text=f'({event.x},{event.y})')
        self.canvas.update()

MousePosition()
       