def perform_operation(num1, num2, operation):
    
    match operation:
        
        case '+':
            add = num1 + num2
            return add
        case '-':
            subtract = num1 - num2
            return subtract
        case '*':
            multiply = num1 * num2
            return multiply
        case '/':
            if num2 == 0:
                return 'Cannot divide by Zero'
            else:
                return num1 / num2
