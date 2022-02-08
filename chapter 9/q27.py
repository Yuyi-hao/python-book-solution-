from ctypes import alignment
from tkinter import * 
class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Compare Interest Rate")
        self.frame1 = Frame(window)
        self.frame1.pack()
        self.frame2 = Frame(window)
        self.frame2.pack()
        self.loanAmount = IntVar()
        self.year = IntVar()
        Label(self.frame1,text="Loan Amount").grid(row=0,column=0)
        Entry(self.frame1,textvariable=self.loanAmount,justify="right").grid(row=0,column=2)
        Label(self.frame1,text="Loan Amount").grid(row=0,column=3)
        Entry(self.frame1,textvariable=self.year,justify="right").grid(row=0,column=4)
        Button(self.frame1,command=self.showresult,text="calculate").grid(row=0,column=5)
        Label(self.frame2,text="Interest Rate \t Monthly Payment \t Total Payment").grid(row=0,column=0,sticky=W)

        window.mainloop()
    def showresult(self):
        loanAmount = self.loanAmount.get()
        loanPeriod = self.year.get()
        interestRate = 5
        increment = 1/8
        self.text = ""
        while (interestRate) <=8:
            monthlyInterestRate = interestRate/1200
            monthlyPayment = loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(loanPeriod*12))
            totalPayment = monthlyPayment*loanPeriod*12
            self.text = self.text + ('{:.3f}% \t \t {:.2f} \t \t {:.2f}\n'.format(interestRate,monthlyPayment,totalPayment))
            interestRate += increment
        Label(self.frame2,text=self.text).grid(row=1,column=0,sticky=W)
        

LoanCalculator()