def add_student(data):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    class_name = input("Enter class name: ")
    student_id = len(data["students"]) + 1
    data["students"].append({"id": student_id, "name": name, "age": age, "class": class_name})
    print(f"Student {name} added successfully.")

def view_students(data):
    print("\n--- Student List ---")
    for student in data["students"]:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Class: {student['class']}")

def delete_student(data):
    student_id = int(input("Enter student ID to delete: "))
    for student in data["students"]:
        if student["id"] == student_id:
            data["students"].remove(student)
            print(f"Student with ID {student_id} deleted successfully.")
            return
    print(f"No student found with ID {student_id}.")

def student_menu(data, save_data):
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(data)
            save_data(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            delete_student(data)
            save_data(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
