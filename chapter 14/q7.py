from curses.ascii import isalpha
from tkinter import *
import urllib.request

def countLetterInLine(line,count):
    line = line.lower()
    for ch in line:
        if isalpha(ch):
            if ch in count:
                count[ch] +=1
            else:
                count[ch] = 1



class OccurrenceOfLetters:
    def __init__(self):
        window = Tk()
        window.title('Occurrence of letters')
        self.URL = StringVar()
        frame0 = Frame(window)
        frame0.pack()
        self.entry = Label(frame0)
        self.result = Canvas(frame0,width=500,height=500)
        self.result.pack(fill='both')

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,text='Enter a URL : ').pack(side=LEFT)
        self.URLEntry = Entry(frame1,textvariable=self.URL)
        self.URLEntry.pack(side=LEFT)
        Button(frame1,text='Show Result',command=self.countLetters).pack(side=LEFT)
        window.mainloop()
    def countLetters(self):
        self.result.delete('bar')
        x = 15
        width = 470/26
        count = self.countEachLetter(self.URL.get())
        heightFactor = 400/max(count.values())
        for i in count:
            self.result.create_rectangle(x,450-(count[i]*heightFactor),x+width,450,tag='bar')
            self.result.create_text(x+width/2,460,text=i)
            x = x+width

    def countEachLetter(self,URL):
        count = {'a':0, 'b':0, 'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        URLobj = urllib.request.urlopen(URL)
        content_string = URLobj.read().decode().lower()
        countLetterInLine(content_string,count)
        return count

        
OccurrenceOfLetters()
