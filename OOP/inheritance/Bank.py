class Bank:
    def __init__(self,name,accno,b):
        self.name=name
        self.accountno=accno
        self.balance=b
    def Display(self):
        print("Customer Name ", self.name)
        print("Customer account number", self.accountno)
        print("Customer Balance ",self.balance)

class Account (Bank): #inheritance
    def __init__(self,name,accno,b,amt):
        super().__init__(name,accno,b)
        self.amount=amt
    def withdraw(self):
        self.balance=self.balance-self.amount
        self.Display()
    def deposit(self):
        self.balance=self.balance+self.amount
        self.Display()

cs=Account("Jatin",102030,50000,1000)

cs.withdraw()
cs.deposit()


