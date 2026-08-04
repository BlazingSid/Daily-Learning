todo = []

while True:
    print("\n------ TO-DO LIST ------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter new task: ")
        todo.append(task)
        print("Task added successfully.")

    elif choice == 2:
        if len(todo) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

            index = int(input("Enter task number to remove: ")) - 1

            if 0 <= index < len(todo):
                removed = todo.pop(index)
                print(removed, "removed.")
            else:
                print("Invalid task number.")

    elif choice == 3:
        if len(todo) == 0:
            print("To-Do List is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

    elif choice == 4:
        todo.clear()
        print("All tasks deleted.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")