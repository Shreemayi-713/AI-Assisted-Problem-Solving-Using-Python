"""
Task 2: Convert Conditional Statements (Java → Python)
This module contains a Python function that checks if a number is positive, negative, or zero.
"""

def check_number(num):
    
    if num > 0:
        return "The number is positive"
    elif num < 0:
        return "The number is negative"
    else:
        return "The number is zero"


# Call the function with different inputs to display results
if __name__ == "__main__":
    print(f"Input: -5 → Output: {check_number(-5)}")
    print(f"Input: 0 → Output: {check_number(0)}")
    print(f"Input: 7 → Output: {check_number(7)}")
