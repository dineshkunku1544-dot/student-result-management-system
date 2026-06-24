import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "D"

    students = load_students()
    students.append({
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    })

    save_students(students)
    print("Student added successfully!")

def view_students():
    students = load_students()
    for student in students:
        print(student)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
