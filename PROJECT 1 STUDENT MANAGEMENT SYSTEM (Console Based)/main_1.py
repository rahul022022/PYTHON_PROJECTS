import json

students = []

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def show_menu():
    print("--- Student Management System ---")
    print("1. Add Student")
    print("2. view_students")
    print("3. search_student")
    print("4. delete_student")
    print("5. Exit")


def add_student():
    sid = int(input("Enter Student Id: "))

    for student in students:
        if student['id'] == sid:
            print("Student Id Already Exist")
            return
    
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Student Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    save_students()
    print("Student Added Successfully")

def view_students():
    if not students:
        print("Student Not Found")
        return
    
    print("\nID | Name | Age | Course")
    print("-" * 30)
    for student in students:
        print(f"{student['id']} | {student['name']} | {student['age']} | {student['course']}")


def search_student():
    sid = int(input("Enter Student Id: "))
    for student in students:
        if student['id'] == sid:
            print("\nStudent found")
            print(student)
            return
    print("Stundet Not Found")

def delete_student():
    sid = int(input("Enter Student Id: "))
    for student in students:
        if student['id'] == sid:
            students.remove(student)
            print("Student Removed Successfully")
    print("Student Not Found")

load_students()

while True:
    show_menu()
    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")