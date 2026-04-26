#Created a simple calculator program that performs various mathematical operations using a user-friendly menu system.
#Performs basic operations like: Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Exponentiation and Square Root. 


import math

while True:
    print("\n----- CALCULATOR -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")
    print("8. Square Root")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice (1-9): "))

        if choice == 9:
            print("Exiting calculator...")
            break

        if choice < 1 or choice > 9:
            print("Invalid choice! Please select 1-9.")
            continue

        try:
            if choice == 8:
                a = float(input("Enter a number: "))
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            print("Result of Addition:", a + b)

        elif choice == 2:
            print("Result of Substraction:", a - b)

        elif choice == 3:
            print("Result of Multiplication:", a * b)

        elif choice == 4:
            if b == 0:
                print("Error: Division by zero")
                continue
            print("Result of Division:", a / b)

        elif choice == 5:
            if b == 0:
                print("Error: Division by zero")
                continue
            print("Result of Floor Division:", a // b)

        elif choice == 6:
            if b == 0:
                print("Error: Modulus by zero")
                continue
            print("Result of Modulus:", a % b)

        elif choice == 7:
            try:
                print("Result of Exponentiation:", a ** b)
            except OverflowError:
                print("Error: Number too large")

        elif choice == 8:
            if a < 0:
                print("Error: Cannot find square root of negative number")
                continue
            print("Result of Square Root:", math.sqrt(a))

    except ValueError:
        print("Invalid input! Please enter numbers only.") 