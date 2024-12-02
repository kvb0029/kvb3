def add_teacher(data):
    name = input("Enter teacher name: ")
    subject = input("Enter subject specialization: ")
    contact = input("Enter contact number: ")
    teacher_id = len(data["teachers"]) + 1
    data["teachers"].append({"id": teacher_id, "name": name, "subject": subject, "contact": contact})
    print(f"Teacher {name} added successfully.")

def view_teachers(data):
    print("\n--- Teacher List ---")
    for teacher in data["teachers"]:
        print(f"ID: {teacher['id']}, Name: {teacher['name']}, Subject: {teacher['subject']}, Contact: {teacher['contact']}")

def delete_teacher(data):
    teacher_id = int(input("Enter teacher ID to delete: "))
    for teacher in data["teachers"]:
        if teacher["id"] == teacher_id:
            data["teachers"].remove(teacher)
            print(f"Teacher with ID {teacher_id} deleted successfully.")
            return
    print(f"No teacher found with ID {teacher_id}.")

def teacher_menu(data, save_data):
    while True:
        print("\n--- Teacher Management ---")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Delete Teacher")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_teacher(data)
            save_data(data)
        elif choice == "2":
            view_teachers(data)
        elif choice == "3":
            delete_teacher(data)
            save_data(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
