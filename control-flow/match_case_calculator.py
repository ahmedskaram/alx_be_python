num1 = float(input('Enter the first number: '))
operations = input('Choose the operation (+, -, *, /):')
num2 = float(input('Enter the second number: '))

match operations:
    case '+':
        result = num1 + num2
        print(f'The result is {result}')
    case '-':
        result = num1 - num2
        print(f'The result is {result}')
    case '*':
        result = num1 * num2
        print(f'The result is {result}')
    case '/':
        if num2 == 0:
            print('Cannot divide by zero.')
        else:
            result = num1 / num2
            print(f'The result is {result}')
    case _:
        print('Invalid operator')
