def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

def calculator():
    print("Welcome to the calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = int(input("Enter the number of the operation (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Error: Invalid operation choice.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"Result: {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {divide(num1, num2)}")
    except ValueError:
        print("Error: Please enter valid numeric values.")

calculator()
