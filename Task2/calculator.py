tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # View tasks
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            i = 0
            while i < len(tasks):
                print(str(i + 1) + ". " + tasks[i])
                i = i + 1

    # Add task
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            i = 0
            while i < len(tasks):
                print(str(i + 1) + ". " + tasks[i])
                i = i + 1

            num = int(input("Enter task number to remove: "))

            if num > 0 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")

    # Exit program
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")