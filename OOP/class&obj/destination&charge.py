class Train:
    def __init__ (self):
        self.src=""
        self.tnm=""
        self.dest=""
        self.charges=0.0
        
    def Getdata(self):
        if self.dest=="Mumbai":
            self.charges=1000
        elif self.dest=="Chennai":
            self.charges=2000
        elif self.dest=="Kolkata":
            self.charges=2500
            
    def InputData(self):
        self.dest=input("Enter destination: ")
        self.tnm=input ("Enter the train name: ")

    def displaydata(self):
        self.Getdata()
        print("Charges are: ",self.charges)


#main
c1=Train()
c1.InputData()
c1.displaydata()
