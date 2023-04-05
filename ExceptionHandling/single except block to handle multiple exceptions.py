try:
    x=int(input("first number: "))
    y=int(input("2nd number: "))
    print(x/y)
    print("I will get printed onnly iof exception is not raised")
    
except(ZeroDivisionError, ValueError) as msg:

    print("Plz prvide suitable integer input only")

'''
except(ZeroDivisionError, ValueError):
    print("Incorrect input")
'''
