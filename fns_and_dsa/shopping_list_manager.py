
shopping_lis = []

while True:
    choice = input('Enter your choice: ')
    
    if choice == '1':
        item = input('Enter item to add: ')
        shopping_lis.append(item)
        
    elif choice == '2':
        item = input('Enter the item to remove: ')
        shopping_lis.remove(item)
    elif choice == '3':
        print(shopping_lis)
    elif choice == '4':
        print('Goodbye!')
    break
