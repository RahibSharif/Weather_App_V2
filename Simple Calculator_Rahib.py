def add(num1, num2):
    sum = num1 + num2
    print(sum)

def subtract(num1, num2):
    subtract = num1 - num2
    print(subtract)

def multiply(num1, num2):
    multiply = num1 * num2
    print(multiply)

def divide(num1, num2):
    try:
        divide = num1 / num2
        print(divide)
    except ZeroDivisionError:
        print("Cannot divide by zero")



while True:
    print("List of operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter a choice: ")

    if choice == "1":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        add(num1,num2)
    elif choice == "2":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        subtract(num1,num2)
    elif choice == "3":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        multiply(num1,num2)
    elif choice == "4":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        divide(num1,num2)
    elif choice == "5":
        print("Exit the program")
        break
    else:
        print("Invalid choice")