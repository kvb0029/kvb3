def schedule_exam(data):
    class_name = input("Enter class name: ")
    subject = input("Enter subject: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    exam_id = len(data["exams"]) + 1
    data["exams"].append({"id": exam_id, "class": class_name, "subject": subject, "date": date})
    print(f"Exam for {class_name} scheduled successfully.")

def view_exams(data):
    print("\n--- Exam List ---")
    for exam in data["exams"]:
        print(f"ID: {exam['id']}, Class: {exam['class']}, Subject: {exam['subject']}, Date: {exam['date']}")

def exam_menu(data, save_data):
    while True:
        print("\n--- Exam Management ---")
        print("1. Schedule Exam")
        print("2. View Exams")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            schedule_exam(data)
            save_data(data)
        elif choice == "2":
            view_exams(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
