#operator overloading

#overloading + operator with objects


class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages + other.pages

b1=Book(100)
b2=Book(200)

no_of_pages=b1+b2

print(type(no_of_pages))
print("Total no. of pages: ",no_of_pages)
