"""
Problem 59: Grade Converter
Error Type: LOGICAL
Difficulty: Medium
"""

def convert_grade(value):
   
    factor = 0.5
    
    print(value // factor) 
     
    return value + factor

print(convert_grade(100))