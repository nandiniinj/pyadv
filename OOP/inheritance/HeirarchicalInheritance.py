class vehicle:
    def __init__(self,nw,cl,engineno,chasisno):
        self.no_of_wheels=nw
        self.color=cl
        self.enginenumber=engineno
        self.chasisnumber=chasisno

    def Displayvehicleinfo(self):
        print(self.enginenumber)
        print(self.chasisnumber)
        print(self.color)
        print(self.no_of_wheels)

class auto(vehicle):
    def __init__(self,nw,cl,eno,cno):
        super().__init__(nw,cl,eno,cno)
    def drive(self):
        print("auto specific driving\n")

class truck(vehicle):
    def __init__(self,nw,cl,eno,cno):
        super().__init__(nw,cl,eno,cno)
    def drive(self):
        print("truck specific driving\n")

#main

truckobj1=truck(5,"brown",102030,2010)
truckobj1.drive()
truckobj1.Displayvehicleinfo()

print("\n---------------------------------------\n")
autoobj=auto(5,"black and yellow",504030,4520)
autoobj.drive()
autoobj.Displayvehicleinfo()


        
        
