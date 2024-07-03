def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 != 0:
                return num1 / num2
            elif num2 == 0:
                return 'cannot divide by zero'
        case _:
            return "enter add, subtract, multiply or divide keyword"
