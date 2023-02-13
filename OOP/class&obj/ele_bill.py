class Ele_Bill:

    def __init__(self):
        self.Cname=''
        self.Pnumber=0
        self.units=0
        self.amount=0.0

    def Calc_Amount(self):
        if self.units<=50:
            self.amount=0
        elif self.units>50 and self.units<=150:
            self.amount=(self.units-50)*0.80
        elif self.units>150 and self.units<=350:
            self.amount= (100*0.80)+(self.units-150)*1.00
        else:
            self.amount= (100*0.80)+(200*1)+((self.units-350)*1.2)

    def Accept(self):
        self.Cname=input("Enter your name: ")
        self.Pnumber=int(input("Enter the product no.: "))
        self.units=int(input("Enter the no. of units: "))
        self.Calc_Amount()

    def Display(self):
        print("---------Your Bill---------")
        print("Name: ", self.Cname)
        print("Product number: ", self.Pnumber)
        print("No. of units: ", self.units)
        print("Amount: ",self.amount)

#main

obj1=Ele_Bill()
obj1.Accept()
obj1.Display()
        
