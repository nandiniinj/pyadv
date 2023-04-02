try:
    x=int(input("first number: "))
    y=int(input("2nd number: "))
    print(x/y)
    print("I will get printed onnly iof exception is not raised")

except ZeroDivisionError:
    print("Can't Divide with zero")

except ValueError:
    print("Please provide int value only")

print("all done")
