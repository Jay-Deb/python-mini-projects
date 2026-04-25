#Created a basic calculator using python
#First only implemented some operations like Addition, Substraction, Multiplication and Division.
#Also will implement other operation like Exponentiation, Square Root, Modulus, Floor Division and etc.


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

operation=str(input("Enter what operation to do (add,sub,mul,div): "))

if operation == "add":
    print("Result of addition of",a,"and",b, "is", a+b)
elif operation == "sub":
    print("Result of Substraction of",a,"and",b, "is", a-b)
elif operation == "mul":
    print("Result of Multiplication of",a,"and",b, "is", a*b)
elif operation == "div":
    print("Result of Division of",a,"and",b, "is", a/b)
else:
    print("Invalid input") 