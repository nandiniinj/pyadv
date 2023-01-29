#if want to display different values


class student:
    '''This provides the student details''' #this is documentation string (it is optional to add this string after creating the class)

    def __init__ (self): #constructor
        #data members or attributes or instance members
        self.rollno=10
        self.name="Harsh"
        
    def Display (self):
        print("The roll number is: ",self.rollno)
        print("The name is: ",self.name)

#main
print(student.__doc__)
s1=student() #creating object or instantiating
s1.Display()

sm=student() #creating another object
sm.Display()
