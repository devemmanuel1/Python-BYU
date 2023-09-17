shopping_cart = []  # List to store the names of the items in the shopping cart

# Display the available options to the user
print("Welcome to the Shopping Cart Program!")

while True:
    print("\nOptions:")
    print("1. Add item")
    print("2. Display items")
    print("3. Quit")

    choice = input("Enter your choice: ")

    # Add item to the cart
    if choice == '1':
        item_name = input("Enter the name of the item: ")
        shopping_cart.append(item_name)
        print("Item added to the cart.")

    # Display the names of the items in the list
    elif choice == '2':
        print("Items in the cart:")
        for item in shopping_cart:
            print(item)

    # Quit the program
    elif choice == '3':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
