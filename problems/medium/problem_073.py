"""
Problem 73: Currency Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_currency(value):
    factor = 0.5
    print( value // factor)
    return value + factor

print(convert_currency(100))