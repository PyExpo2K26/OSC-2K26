"""
Problem 67: Temperature Validator
Error Type: LOGIC
Difficulty: Medium
"""

# Generic logic for Temperature Validator
try:
    def run():
        x = 10
        y = 0
        return x / y

    run()
except ZeroDivisionError:
    print("ZeroDivisionError")
