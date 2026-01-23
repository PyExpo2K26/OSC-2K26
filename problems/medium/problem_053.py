"""
Problem 53: Budget Validator
Error Type: LOGIC
Difficulty: Medium
"""

try:
    def run():
        x = 10
        y = 0
        return x / y

    run()
except ZeroDivisionError:
    print("ZeroDivisionError")
