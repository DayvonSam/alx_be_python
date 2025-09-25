# test_arithmetic.py
from arithmetic_operations import perform_operation

assert perform_operation(5, 6, "add") == 11
assert perform_operation(10, 3, "subtract") == 7
assert perform_operation(4, 2, "multiply") == 8
assert perform_operation(9, 3, "divide") == 3
assert perform_operation(9, 0, "divide") == "Cannot divide by zero."
assert perform_operation(1, 1, "unknown") == "Invalid operation."

print("All tests passed.")