############################################################################
try:
    
    num1 = int(input("Enter the first number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))
    
    match operation:
        case "+":
            result = num1 + num2
            print(f'The result is: {result}')
        case "-":
            result = num1 - num2
            print(f'The result is: {result}')
        case "*":
            result = num1 * num2
            print(f'The result is: {result}')
        case "/":
            if num2 == 0:
                raise ZeroDivisionError('Cannot divide by zero.')
            result = num1 / num2
            print(f'The result is: {result}')
        case _:
            print("Please enter valid operation.")
            
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Please enter valid numbers.")

############################################################################

# A simpler way to calculate without exception handling

num1 = int(input("Enter the first number: "))
operation = input("Choose the operation (+, -, *, /): ")
num2 = int(input("Enter the second number: "))
    
match operation:
    case "+":
        result = num1 + num2
        print(f'The result is: {result}')
    case "-":
        result = num1 - num2
        print(f'The result is: {result}')
    case "*":
        result = num1 * num2
        print(f'The result is: {result}')
    case "/":
        if num2 == 0:
            print('Cannot divide by zero.')
        result = num1 / num2
        print(f'The result is: {result}')
    case _:
        print("Please enter valid operation.")

############################################################################