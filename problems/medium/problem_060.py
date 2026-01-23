"""
Problem 60: Grade Validator
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
