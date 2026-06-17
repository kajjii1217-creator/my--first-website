students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    marks = int(input("Enter your marks: "))
    if marks >= 40:
        grade = "Pass"
    else:
        grade = "Fail"
    students.append({"name": name, "age": age, "marks": marks, "grade": grade})
    print("Student added! ✅")

def show_students():
    if len(students) == 0:
        print("No students found! ❌")
    else:
        for student in students:
            print("---")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])

while True:
    print("\n1. Add student")
    print("2. Show students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! ❌")
        