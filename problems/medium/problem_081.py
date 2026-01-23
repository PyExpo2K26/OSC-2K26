"""
Problem 81: Distance Validator
Error Type: LOGIC
Difficulty: Medium
"""

# Generic logic for Distance Validator
try:
    def run():
        x = 10
        y = 0
        return x / y

    run()
except ZeroDivisionError:
    print("ZeroDivisionError")
