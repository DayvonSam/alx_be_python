def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.

    Parameters:
    - numerator: value that should convert to float
    - denominator: value that should convert to float

    Returns:
    - A string with the result or an error message:
      * "The result of the division is <result>"
      * "Error: Cannot divide by zero."
      * "Error: Please enter numeric values only."
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
