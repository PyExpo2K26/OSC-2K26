"""
Problem 81: Distance Validator
Error Type: LOGIC
Difficulty: Medium
"""

# Generic logic for Distance Validator
def run():
    x = 10
    y = 0
    try:    
     return x / y
    except ZeroDivisionError:
        print("Cannot divide by 0")

run()