cart = []

while True:
    print("\n------ SHOPPING CART ------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == 2:
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for i in range(len(cart)):
                print(i + 1, ".", cart[i])

            index = int(input("Enter item number to remove: ")) - 1

            if 0 <= index < len(cart):
                removed = cart.pop(index)
                print(removed, "removed from cart.")
            else:
                print("Invalid item number.")

    elif choice == 3:
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nShopping Cart:")
            for i in range(len(cart)):
                print(i + 1, ".", cart[i])

    elif choice == 4:
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nItems Purchased:")
            for item in cart:
                print("-", item)

            print("Thank you for shopping!")
            cart.clear()

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")