#Created a student result manager
#Allows operations like: Add student details, View student records, Check student result, Update student marks and Delete student records

student = {}

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

while True:
    print("\n----- STUDENT RESULT MANAGER -----")
    print("1. Add Student's details")
    print("2. View Student's details")
    print("3. Check Result")
    print("4. Update Student's details")
    print("5. Delete Student's details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        try:
            marks = int(input("Enter student marks (0-100): "))
            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100!")
                continue
        except ValueError:
            print("Invalid marks input!")
            continue

        student[name] = marks
        print(f"{name}'s details added successfully!")

    elif choice == "2":
        if not student:
            print("No data available!")
        else:
            print("\n--- Student List ---")
            for name, marks in student.items():
                grade = calculate_grade(marks)
                print(f"{name} : {marks} ({grade})")

    elif choice == "3":
        name = input("Enter student name: ").strip()

        if name in student:
            marks = student[name]
            grade = calculate_grade(marks)

            print(f"Marks: {marks}")
            print(f"Grade: {grade}")

            if marks >= 40:
                print("Result: Pass")
            else:
                print("Result: Fail")
        else:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter student name to update: ").strip()

        if name in student:
            try:
                new_marks = int(input("Enter new marks (0-100): "))
                if new_marks < 0 or new_marks > 100:
                    print("Marks should be between 0 and 100!")
                    continue
            except ValueError:
                print("Invalid input!")
                continue

            student[name] = new_marks
            print(f"{name}'s marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        name = input("Enter student name to delete: ").strip()

        if name in student:
            del student[name]
            print(f"{name}'s detail deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid input!") 