### Project 2: Simple Calculator
# Code

````
def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    if operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operation.")

calculator()