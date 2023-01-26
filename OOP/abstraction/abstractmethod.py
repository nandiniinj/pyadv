from abc import *         #imp to write an abstract method

class Shape(ABC):
    @abstractmethod     #decorator

    def area(self):    #abstract method
        pass
    
    def display(self):   #concrete method
        print("I am in shape class")

class rectangle(Shape):

    def __init__ (self):
        self.l=10
        self.b=20
    def area (self):
        print("Area: ",self.l*self.b)
        self.display()

class circle (Shape):

    def __init__ (self):
        self.r=3.5

    def area(self):
        print("Area: ",3.14*(self.r**2))
        self.display()

class triangle (Shape):   #abstract class
    pass

#main

obj1=rectangle()
obj1.area()

obj2=circle()
obj2.area()

#obj=Shape()  #error
#obj3=triangle()   #error
