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
        
        if operator == 'sin':
            result = math.sin(math.radians(num))  # degrees to radians
        elif operator == 'cos':
            result = math.cos(math.radians(num))
        elif operator == 'tan':
            result = math.tan(math.radians(num))
        elif operator == 'log':
            if num > 0:
                result = math.log10(num)  # log base 10
            else:
                return "Error: log undefined for non-positive numbers"
        
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Cannot divide by zero!"
        elif operator == '^':
            result = num1 ** num2
        else:
            return "Invalid operator!"

    return f"Result: {result}"

print(calculator())
