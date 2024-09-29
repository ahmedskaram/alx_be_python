shopping_lis = []  # Initialize the shopping list once, outside the loop

while True:
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    choice = input('Enter your choice: ').strip()
    
    if choice == '1':
        item = input('Enter item to add: ').strip()
        shopping_lis.append(item)
        print(f"'{item}' has been added to the list.")
        
    elif choice == '2':
        item = input('Enter the item to remove: ').strip()
        if item in shopping_lis:
            shopping_lis.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' not found in the list.")
    
    elif choice == '3':
        if shopping_lis:
            print("\nCurrent Shopping List:")
            for index, item in enumerate(shopping_lis, start=1):
                print(f"{index}. {item}")
        else:
            print("Your shopping list is empty.")
    
    elif choice == '4':
        print('Goodbye!')
        break  # Exit the loop to end the program
    
    else:
        print('Invalid choice. Please try again.')
