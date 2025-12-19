
# ------------------------------
# Simple Calculator Program
# ------------------------------

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero"
    else:
        return a / b


print(" Welcome to Simple Calculator ")

# Loop to keep calculator running
while True:
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == "5":
        print("Calculator Closed")
        break

    # Check valid choice
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        print("Result:", result)

    else:
        print("Invalid choice! Please try again.")
