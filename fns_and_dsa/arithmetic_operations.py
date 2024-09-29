def perform_operation(num1, num2, operation):
    
    if operation == '+':
        add = num1 + num2
        return add
    elif operation == '-':
        subtract = num1 - num2
        return subtract
    elif operation == '*':
        multiply = num1 * num2
        return multiply
    elif operation == '/':
        if num2 == 0:
            return 'Cannot divide by Zero'
        else:
            return num1 / num2
