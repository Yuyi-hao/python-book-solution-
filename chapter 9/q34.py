from tkinter import * 
class AddressBook:
    def __init__(self):
        window = Tk()
        window.title("Compare Interest Rate")
        self.frame1 = Frame(window)
        self.frame1.pack()
        self.frame2 = Frame(window)
        self.frame2.pack()
        self.frame3 = Frame(window)
        self.frame3.pack()
        self.frame4 = Frame(window)
        self.frame4.pack()
        self.frame5 = Frame(window)
        self.frame5.pack()
        self.name = StringVar() 
        self.street = StringVar()
        self.city = StringVar() 
        self.state = StringVar()
        self.zip = StringVar()

        Label(self.frame1,text="Name : ").grid(row=0,column=0,sticky=W)
        Entry(self.frame1,textvariable=self.name,justify="left",width=40).grid(row=0,column=2,sticky=W)

        Label(self.frame2,text="Street : ").grid(row=1,column=0,sticky=W)
        Entry(self.frame2,textvariable=self.street,justify="left",width=40).grid(row=1,column=2,sticky=W)
        Label(self.frame3,text="City : ").grid(row=2,column=0,sticky=W)
        Entry(self.frame3,textvariable=self.city,justify="left",width=15).grid(row=2,column=1,sticky=W)
        Label(self.frame3,text="State : ").grid(row=2,column=2,sticky=W)
        Entry(self.frame3,textvariable=self.state,justify="left",width=10).grid(row=2,column=3,sticky=W)
        Label(self.frame3,text="ZIP : ").grid(row=2,column=4,sticky=W)
        Entry(self.frame3,textvariable=self.zip,justify="left",width=5).grid(row=2,column=5,sticky=W)

        Button(self.frame4,command=self.showresult,text="Add").grid(row=3,column=0)
        Button(self.frame4,command=self.showresult,text="First").grid(row=3,column=1)
        Button(self.frame4,command=self.showresult,text="Next").grid(row=3,column=2)
        Button(self.frame4,command=self.showresult,text="Previous").grid(row=3,column=3)
        Button(self.frame4,command=self.showresult,text="Last").grid(row=3,column=4)

        Label(self.frame5,text="Entered Address : ").grid(row=0,column=0,sticky=W)

        window.mainloop()
    def showresult(self):
        name = self.name.get()
        street = self.street.get()
        city = self.city.get() 
        state = self.state.get()
        zip  = self.zip.get()
        text = f'Name : {name}\nStreet : {street}\nCity : {city}\nState : {state}\nZIP : {zip}\n'
        Label(self.frame5,text= text).grid(row=1,column=0,sticky=W)

AddressBook()