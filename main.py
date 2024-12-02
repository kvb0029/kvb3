import json
from students import student_menu
from teachers import teacher_menu
from classes import class_menu
from exams import exam_menu

# Load and save data globally
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"students": [], "teachers": [], "classes": [], "exams": []}

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Main menu
def main_menu():
    data = load_data()
    while True:
        print("\n--- School Management System ---")
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Class Management")
        print("4. Exam Management")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            student_menu(data, save_data)
        elif choice == "2":
            teacher_menu(data, save_data)
        elif choice == "3":
            class_menu(data, save_data)
        elif choice == "4":
            exam_menu(data, save_data)
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
