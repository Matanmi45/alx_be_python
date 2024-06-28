num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
        # pattern 1
        case "+":
            print(f"The result is {num1 + num2}")
        # pattern 2
        case "-":
            print(f"The result is {num1 - num2}")
        # pattern 3
        case "*":
            print(f"The result is {num1 * num2}")
        # default pattern
        case "/" if num2 > 0:
            print(f"The result is {num1 / num2}")
        case "/" if num2 == 0:
            print("Cannot divide by zero.")

