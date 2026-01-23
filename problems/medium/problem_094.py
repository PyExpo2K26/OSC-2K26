"""
Problem 94: Time Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_time(value):
    factor = 0.5
    print(value // factor)
    return value + factor

print(convert_time(100))