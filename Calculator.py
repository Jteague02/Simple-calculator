def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x/ y

while True:
    choice = input("Select type of operation: ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '+':
            print(add(num1, num2))
        elif choice == '-':
            print(subtract(num1, num2))
        elif choice == '*':
            print(multiply(num1, num2))
        elif choice == '/':
            print(divide(num1, num2))

        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid operation")

        
