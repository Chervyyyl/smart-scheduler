exams = []

# this function let the user add a new exam to the schedule
def add_exam():
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter exam room: ")
    exam = {"name": name, "date": date, "time": time, "room": room}
    exams.append(exam)
    print("Exam added successfully!\n")

# this function displays all scheduled exams
def view_exams():
    if not exams:
        print("No exams scheduled.\n")
        return
    for idx, exam in enumerate(exams, 1):
        print(f"{idx}. Name: {exam['name']}, Date: {exam['date']}, Time: {exam['time']}, Room: {exam['room']}")
    print()

# this function allow the user to edit an existing exam detail
def edit_exam():
    view_exams()
    if not exams:
        return
    try:
        idx = int(input("Enter the number of the exam to edit: ")) - 1
        if 0 <= idx < len(exams):
            name = input(f"Enter new name ({exams[idx]['name']}): ") or exams[idx]['name']
            date = input(f"Enter new date ({exams[idx]['date']}): ") or exams[idx]['date']
            time = input(f"Enter new time ({exams[idx]['time']}): ") or exams[idx]['time']
            room = input(f"Enter new room ({exams[idx]['room']}): ") or exams[idx]['room']
            exams[idx] = {"name": name, "date": date, "time": time, "room": room}
            print("Exam updated successfully!\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# this function remove or delete a selected exam from the schedule
def delete_exam():
    view_exams()
    if not exams:
        return
    try:
        idx = int(input("Enter the number of the exam to delete: ")) - 1
        if 0 <= idx < len(exams):
            exams.pop(idx)
            print("Exam deleted successfully!\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# this function displays the main menu and handles user input
def main_menu():
    # this is the main program loop that shows the menu and handles user choices
    while True:
        print("Exam Scheduler Menu:")
        print("1. Add exam")
        print("2. View exams")
        print("3. Edit exam")
        print("4. Delete exam")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
