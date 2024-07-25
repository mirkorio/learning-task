#marc_christian_tumaneng_bscs3a - Error Exception - Activity
# Import the math module for mathematical operations
import math

# Dictionary to store results of operations
results_dictionary = {}

# Function to perform mathematical operations
def perform_operation(operation, x, y):
    # Addition
    if operation == '+':
        return x + y
    # Subtraction
    elif operation == '-':
        return x - y
    # Multiplication
    elif operation == '*':
        return x * y
    # Division
    elif operation == '/':
        # Check for division by zero
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    # Exponentiation
    elif operation == '**':
        return x ** y
    # Square root
    elif operation == 'sqrt':
        # Check for square root of a negative number
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)
    # Invalid operation
    else:
        raise ValueError("Invalid operation")

# Function to get user input for numbers and operation
def get_user_input():
    try:
        # Get the first number from the user
        x_input = input("\nEnter the first number (or 'q' to quit): ")
        if x_input == 'q':
            return 'q', None, None

        x = float(x_input)
        # Get the second number from the user
        y = float(input("\nEnter the second number: "))
        # Get the operation from the user
        operation = input("\nEnter the operation (+, -, *, /, ** for exponentiation, sqrt for square root): ")

        # Validate the operation input
        while operation not in ['+', '-', '*', '/', '**', 'sqrt', 'q']:
            print("\nError: Invalid operation")
            operation = input("\nEnter the operation (+, -, *, /, ** for exponentiation, sqrt for square root): ")

        return operation, x, y

    # Handle invalid input (non-numeric input)
    except ValueError:
        print("\nError: Invalid input. Please enter a valid number.")
        return get_user_input()

try:
    # Main loop to get user input and perform operations until the user quits
    while True:
        operation, x, y = get_user_input()

        if operation == 'q':
            break

        try:
            # Try performing the operation and print the result
            result = perform_operation(operation, x, y)
            print("\nResult:", result)
            # Save the result to the dictionary
            results_dictionary[f"({x}, {y}, '{operation}' )"] = result  

        # Handle division by zero exception
        except ZeroDivisionError as e:
            print("\nError:", str(e))

        # Handle other value errors (e.g., square root of a negative number)
        except ValueError as e:
            print("\nError:", str(e))
            
        # This block always executes, whether an exception occurred or not.
        print("This block always executes, whether an exception occurred or not.")      

finally:
    # Display previous results
    print("\nPrevious Results:" if results_dictionary else "")
    print("\n".join([f"{key} => {value}" for key, value in results_dictionary.items()]))

    
