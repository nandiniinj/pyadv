class product:

    def __init__(self):
        self.productno=1021
        self.productname="Juice"
        self.price="Rs. 65"
        
    def showdata (self):
        print(self.productno)
        print(self.productname)
        print(self.price)

p1=product()
p1.showdata()
