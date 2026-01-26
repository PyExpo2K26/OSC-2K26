"""
Problem 51: Budget Calculator
Error Type: LOGICAL
Difficulty: Medium
"""

def calculate_budget(items):
    """
    calculate_budget returns the total of the array passed 

    paramater calculate_budget(items) -> type of items : array

    """
    total = 0
   
    for item in items:
        total  += item 
    return total

#test cases :
assert calculate_budget([10,20,30])==60
assert calculate_budget([])==0
assert calculate_budget([-10,20])==10
