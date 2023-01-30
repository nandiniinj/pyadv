#instance variables can be defined inside the constructor and inside the method and outside the class also
class Books:
    def __init__(self,bno,bname,bprice):

        #instance variables inside the constructor
        self.bno=bno
        self.bname=bname
        self.bprice=bprice

        
    def Display(self):

        self.bauthor="ABC"   #instance variables inside the method
        print(self.bno)
        print(self.bname)
        print(self.bprice)
        print(self.bauthor)
        
#main
b1=Books(101,"Java",299) #creating an object
print(b1.__dict__)

b1.Display()
print(b1.__dict__)

b2=Books(101,"Java",299)
print(b2.__dict__)


b2.pageno=350 #outside the class
b2.Display()
print(b2.__dict__)


