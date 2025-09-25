# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.
    operation: 'add', 'subtract', 'multiply', 'divide'
    For division by zero, return the string "Cannot divide by zero."
    """
    # normalize operation string safely (allow non-string by converting)
    try:
        op = str(operation).strip().lower()
    except Exception:
        op = ""

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        # handle division by zero explicitly
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operation."
