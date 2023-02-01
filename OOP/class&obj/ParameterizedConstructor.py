class student:
    '''This provides the student details''' #this is documentation string (it is optional to add this string after creating the class)

    def __init__ (self,r,n): #parameterized constructor
        #data members or attributes or instance members
        self.rollno=r
        self.name=n
        
    def Display (self):
        print("The roll number is: ",self.rollno)
        print("The name is: ",self.name)

#main
print(student.__doc__)
s1=student(10,"Harsh") #creating object or instantiating
s1.Display()

sm=student(11,"Priya") #creating another object
sm.Display()
