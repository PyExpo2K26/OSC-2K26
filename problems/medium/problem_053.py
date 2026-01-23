"""
Problem 53: Budget Validator
Error Type: LOGIC
Difficulty: Medium
"""

 
def run():
    x = 10
    y = 0
    try:
        return x / y
    except ZeroDivisionError:
        print("cannot divide by zero")
run()