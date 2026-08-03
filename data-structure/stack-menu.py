# Predefined stack
stack = ["Maths", "Science", "English", "History", "Geography", "Hindi", "Economics", "Computer",  "Science", "Environmental Science", "Social Studies" ]

while True:
    print("\n------ STACK MENU ------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = (input("Enter value to push: "))
        stack.append(value)
        print(value, "pushed into stack.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow!")
        else:
            removed = stack.pop()
            print(removed, "removed from stack.")

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements (Top to Bottom):")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")