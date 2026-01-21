"""
Problem 1: Simple Calculator
Error Type: SYNTAX

PROBLEM DESCRIPTION:
--------------------
Create a simple calculator function that performs basic arithmetic operations.
The function should take two numbers and an operation string, then return the result.

Currently, the code contains a SYNTAX ERROR that prevents it from running.
Your task is to identify and fix the bug.

EXPECTED BEHAVIOR:
------------------
- Addition: calculate(5, 3, '+') → 8
- Subtraction: calculate(10, 4, '-') → 6
- Unknown operation: calculate(5, 3, '*') → "Unknown operation"

INSTRUCTIONS:
1. Identify the syntax error in the code below
2. Fix the bug to make the code run without errors
3. Ensure all test cases pass
4. The function should work with any two numbers and valid operations

Difficulty: Easy
"""

def calculate(a, b, op):
    """
    Perform a basic arithmetic operation on two numbers.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        op: Operation as a string ('+' or '-')
    
    Returns:
        The result of the operation, or "Unknown operation" if op is not recognized
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return "Unknown operation"


# Test Cases
def run_tests():
    """Run test cases to verify the calculator works correctly."""
    # Test case 1: Addition
    assert calculate(5, 3, '+') == 8, "Addition test failed"
    
    # Test case 2: Subtraction
    assert calculate(10, 4, '-') == 6, "Subtraction test failed"
    
    # Test case 3: Unknown operation
    assert calculate(5, 3, '*') == "Unknown operation", "Unknown operation test failed"
    
    # Test case 4: Negative numbers
    assert calculate(-5, 3, '+') == -2, "Negative number addition test failed"
    
    # Test case 5: Decimal numbers
    assert calculate(5.5, 2.5, '+') == 8.0, "Decimal addition test failed"
    
    print("✓ All test cases passed!")


# Main execution
if __name__ == "__main__":
    # Example usage
    result = calculate(5, 3, '+')
    print(f"calculate(5, 3, '+') = {result}")
    
    # Run all tests
    run_tests()