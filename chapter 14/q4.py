from ctypes import alignment
from curses.ascii import isalpha
from tkinter import *
from tkinter.filedialog import askopenfilenames
import tkinter.messagebox

def countLetterInLine(line,count):
    line = line.lower()
    for ch in line:
        if isalpha(ch):
            if ch in count:
                count[ch] +=1
            else:
                count[ch] = 1

    
# def countEachLetter(filename):
#     count = {'a':0, 'b':0, 'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
#     while True:
#         try:
#             fileobj = open(filename,'r')
#             break
#         except FileNotFoundError:
#             tkinter.messagebox.showerror("Show Error",f"No Such or directory : {filename}")
#     for line in fileobj:
#         countLetterInLine(line,count)
    
#     return count



class OccurrenceOfLetters:
    def __init__(self):
        window = Tk()
        window.title('Occurrence of letters')
        self.filename = StringVar()
        frame0 = Frame(window)
        frame0.pack()
        self.entry = Label(frame0)
        self.result = Label(frame0,text="No file selected",anchor='w')
        self.result.pack(fill='both')

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,text='Enter a filename : ').pack(side=LEFT)
        self.filenameEntry = Entry(frame1,textvariable=self.filename)
        self.filenameEntry.pack(side=LEFT)
        Button(frame1,text='Browse',command=self.openFile).pack(side=LEFT)
        Button(frame1,text='Show Result',command=self.countLetters).pack(side=LEFT)
        window.mainloop()
    def countLetters(self):
        count = self.countEachLetter(self.filename.get())
        s = ''
        for i in count:
            if count[i] > 0:
                s += f" {i} appears  {count[i] } "+'times\n' if count[i]>0 else 'time\n'
        self.result["text"] = s
        self.result["anchor"] = 'w'

    def openFile(self):
        fileName = str(askopenfilenames())
        fileName = fileName.replace("('","").replace("',)","")
        self.filenameEntry.insert(END,fileName)
    
    def countEachLetter(self,filename):
        count = {'a':0, 'b':0, 'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        while True:
            try:
                fileobj = open(filename,'r')
                break
            except FileNotFoundError:
                tkinter.messagebox.showerror("Show Error",f"No Such or directory : {filename}")
                self.openFile()
        for line in fileobj:
            countLetterInLine(line,count)
        
        return count

        
OccurrenceOfLetters()
