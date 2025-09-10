"""
This is a chatGPT written simple calculator
"""

import math

def calculator():
    print("Simple Calculator")
    print("Operators: +, -, *, /, ^, sin, cos, tan, log")
    
    operator = input("Enter operator: ").lower()

    if operator in ['sin', 'cos', 'tan', 'log']:
        num = float(input("Enter number: "))
        match operator:
            case 'sin':
                result = math.sin(math.radians(num))
            case 'cos':
                result = math.cos(math.radians(num))
            case 'tan':
                result = math.tan(math.radians(num))
            case 'log':
                if num > 0:
                    result = math.log10(num)
                else:
                    return "Error: log undefined for non-positive numbers"
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        match operator:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "Error: Cannot divide by zero!"
            case '^':
                result = num1 ** num2
            case _:
                return "Invalid operator!"

    return f"Result: {result}"

print(calculator())
