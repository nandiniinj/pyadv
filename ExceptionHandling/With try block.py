print("statement 1")
try:
    num1=int(input("Enter the first number: "))
    num2= int(input("Enter the second number: "))
    num3=num1/num2
    print("statement 2: I will execute or not")

except ZeroDivisionError:
    print("Cannot divide by zero")
    num3=None

print(num3)
print("statement 3")
