class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def setId(self,newId):
        self.__id = newId
        return self.__id
    def setBalance(self,newBalance):
        self.__balance = newBalance
        return self.__balance
    def setAnnualInterstRate(self,newInterestRate):
        self.__annualInterestRate = newInterestRate
        return self.__annualInterestRate
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/1200
    def getMonthlyInterest(self):
        monthlyInterest = self.__balance*self.getMonthlyInterestRate()
        return monthlyInterest
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance = self.__balance-amount
        return self.__balance
    def deposits(self,amount):
        self.__balance = self.__balance+amount
        return self.__balance

def main():
    account1 = Account(1122,20000,4.5)
    print('Account details')
    print('Account id : {}\nBalance : {:.2f}\nAnnual interest rate : {:.2f}'.format(account1.getId(),account1.getBalance(),account1.getAnnualInterestRate()))
    account1.withdraw(2500)
    print('Monthly interest rate : {:.5f}\nMonthly interest : {:.2f}'.format(account1.getMonthlyInterestRate(),account1.getMonthlyInterest()))
    print('Withdraw amount {:.2f}'.format(2500))
    print('Your balance : {:.2f}'.format(account1.getBalance()))
    account1.deposits(3000)
    print('Deposit amount {:.2f}'.format(3000))
    print('Your balance : {:.2f}'.format(account1.getBalance()))

main()