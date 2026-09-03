students = {}

while True:
    print("\n--- MENU ---")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").strip().upper()

    # 1. Add a student
    if choice == 'A':
        name = input("Enter student name: ").strip()
        if name in students:
            print(f"Error: {name} already exists. Use Option B to update marks.")
        else:
            try:
                marks = int(input(f"Enter marks for {name}: "))
                students[name] = marks
                print(f"Successfully added {name} with marks: {marks}")
            except ValueError:
                print("Invalid input! Marks must be an integer.")

    # 2. Update marks
    elif choice == 'B':
        name = input("Enter student name to update: ").strip()
        if name in students:
            try:
                new_marks = int(input(f"Enter new marks for {name}: "))
                students[name] = new_marks
                print(f"Updated {name}'s marks to: {new_marks}")
            except ValueError:
                print("Invalid input! Marks must be an integer.")
        else:
            print(f"Error: {name} not found in records.")

    # 3. Search for a student
    elif choice == 'C':
        name = input("Enter student name to search: ").strip()
        if name in students:
            print(f"Result: {name} scored {students[name]} marks.")
        else:
            print(f"Result: {name} is not in the records.")

    # 4. Display all students and marks
    elif choice == 'D':
        if not students:
            print("No student records available.")
        else:
            print("\n--- Student Records ---")
            for name, marks in students.items():
                print(f"{name}: {marks}")

    # Exit program
    elif choice == 'E':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select A, B, C, D, or E.")