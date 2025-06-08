# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        num1: The first number (float or int).
        num2: The second number (float or int).
        operation: A string indicating the operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        The result of the arithmetic operation, or an error message for invalid inputs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

