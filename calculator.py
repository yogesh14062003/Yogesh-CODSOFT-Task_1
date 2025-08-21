# calculator.py

def calculate():
    """
    Performs a basic arithmetic calculation based on user input.
    """
    try:
        # Prompt user for the first number
        num1 = float(input("Enter the first number: "))

        # Prompt user for the second number
        num2 = float(input("Enter the second number: "))

        # Prompt user for the operation
        operation = input("Choose an operation (+, -, *, /): ")

        # Perform the calculation based on the chosen operation
        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                print("Error: Cannot divide by zero. 🚫")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            # Handle invalid operation input
            print("Invalid operation selected. Please choose from +, -, *, /.")

    except ValueError:
        # Handle cases where input is not a number
        print("Invalid input. Please enter valid numbers. 🔢")
    except Exception as e:
        # Handle other potential errors
        print(f"An error occurred: {e}")

# Run the calculator function
if __name__ == "__main__":
    calculate()