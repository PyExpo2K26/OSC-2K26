"""
Problem 80: Distance Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_distance(value):
    factor = 0.5
    print(value // factor)
    return value + factor

print(convert_distance(100))