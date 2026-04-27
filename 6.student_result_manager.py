#Created a student result manager
#We can add student details, view details, check result of students and exit when needed
#also implement other features in future 


student = {}

while True:
    print("/n-----STUDENT RESULT MANAGER-----")
    print("1. Add student ")
    print("2. View student Details")
    print("3. Check result")
    print("4. Exit")

    choice=input("Enter your choice:")

    if choice == "1":
        name=input("Enter student name: ")
        marks=int(input("Enter student marks: "))
        student[name]=marks
        print(f"{name}'s details successfully added!!")

    elif choice=="2":
        if not student:
            print("No data available!!")
        else:
            for name,marks in student.items():
                print(name,":",marks)

    elif choice=="3":
        name=input("Enter student name: ")
        if name in student:
            marks=student[name]
            if marks>=40:
                print("Pass!")
            else:
                print("Fail!")
        else:
            print("Student not found!!")

    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("Invalid input!!")