"""
Problem 87: Weight Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_weight(value):
    factor = 0.5
    print(value // factor)
    return value * factor

print(convert_weight(100))