def schedule_class(data):
    name = input("Enter class name: ")
    teacher_id = int(input("Enter teacher ID: "))
    time = input("Enter class time (e.g., 10:00 AM): ")
    for teacher in data["teachers"]:
        if teacher["id"] == teacher_id:
            class_id = len(data["classes"]) + 1
            data["classes"].append({"id": class_id, "name": name, "teacher": teacher["name"], "time": time})
            print(f"Class {name} scheduled successfully.")
            return
    print(f"No teacher found with ID {teacher_id}.")

def view_classes(data):
    print("\n--- Class List ---")
    for class_data in data["classes"]:
        print(f"ID: {class_data['id']}, Name: {class_data['name']}, Teacher: {class_data['teacher']}, Time: {class_data['time']}")

def class_menu(data, save_data):
    while True:
        print("\n--- Class Management ---")
        print("1. Schedule Class")
        print("2. View Classes")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            schedule_class(data)
            save_data(data)
        elif choice == "2":
            view_classes(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
