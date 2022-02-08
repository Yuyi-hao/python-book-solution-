from tkinter import * 
class FlashingText:
    def __init__(self,text):
        self.text = text
        window = Tk()
        window.title("Flashing Text")
        self.width = 250
        self.height = 100
        self.canvas = Canvas(window,height=self.height,width=self.width,bg="White")
        self.canvas.pack()
        self.variable = True
        while True:
            self.showText()
            self.canvas.after(1000) 
            self.canvas.update()
        window.mainloop()
    def showText(self):
        if self.variable:
            self.canvas.delete("Text")
            self.variable = False
        else:
            self.canvas.create_text(self.width/2,self.height/2,text=self.text,tags = "Text")
            self.variable = True

def main():
    text = input("Enter the text you want to display : ")
    FlashingText(text)
main()