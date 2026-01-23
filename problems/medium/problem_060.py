"""
Problem 60: Grade Validator
Error Type: LOGIC
Difficulty: Medium
"""

def run():
    x = 10
    y = 0
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by 0")

run()