class Course:
    def __init__(self):
        self.regno=0
        self.score=0.0
        self.fees=0.0
        
    def setcourse(self):
        if self.score>=9.0 and self.score<=10.0:
            self.cname="Clinical Psychology"
            self.fees=10000.0
        elif self.score>=8.0 and self.score<9.0:
            self.cname="Corporate Counselling"
            self.fees=8000.0
        elif self.score>=5.0 and self.score<8.0:
            self.cname="Guidance and Counselling"
            self.fees=6000.0
        else:
            self.cname="Your score is very low, you are not eligible."
            self.fees=0.0

    def getdata(self):
        self.regno=int(input("Enter your registration no.: "))
        self.score=float(input("Enter your score: "))
        self.setcourse() #calling the function within the class so no need of creating the object

    def display(self):
        #print("Your registration no. is: ",self.regno)
        #print("Your score is: ",self.score)
        print("Your course alloted is: ",self.cname)
        print("Your fees is: ",self.fees)

#main

t=int(input("Enter the number of entries you want to insert: "))
print("-------------------------------------------------")
while t>0:
    
    c1=Course()
    c1.getdata()
    print("Your course details are:- ")
    c1.display()

    print("-------------------------------------------------")

    t-=1
        
