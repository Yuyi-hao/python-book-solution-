from tkinter import *
class FutureValueCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment calculator")
        window.minsize(250,115)
        window.maxsize(250,115)
        Label(window,text="Investment Amount : ").grid(row=0,column=0,sticky=W)
        Label(window,text="Year : ").grid(row=1,column=0,sticky=W)
        Label(window,text="Annual Interest Rate : ").grid(row=2,column=0,sticky=W)
        Label(window,text="Future Value : ").grid(row=3,column=0,sticky=W)
        
        self.investmentAmount = DoubleVar()
        Entry(window,textvariable = self.investmentAmount,justify=RIGHT).grid(row=0,column=1)
        
        self.years = IntVar()
        Entry(window,textvariable=self.years,justify=RIGHT).grid(row=1,column=1)
        
        self.annualInterestRate = DoubleVar()
        Entry(window,textvariable=self.annualInterestRate,justify=RIGHT).grid(row=2,column=1)


        self.futureAmountvar = StringVar()
        Label(window,textvariable=self.futureAmountvar).grid(row=3,column=1,sticky=E)

        Button(window,text="Calculate",command=self.futureValue).grid(row=4,column=1,sticky=E)
        window.mainloop()

    def futureValue(self):
        monthlyinterestRate = float(self.annualInterestRate.get())/1200
        self.futureAmount = float(self.investmentAmount.get())*((1+monthlyinterestRate)**(int(self.years.get()*12)))
        self.futureAmountvar.set("{:.2f}".format(self.futureAmount))
      
FutureValueCalculator()