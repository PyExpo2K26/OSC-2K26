"""
Problem 67: Temperature Validator
Error Type: LOGIC
Difficulty: Medium
"""

# Generic logic for Temperature Validator
def run():
    x = 10
    y = 0
    try: 
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by 0")

run()