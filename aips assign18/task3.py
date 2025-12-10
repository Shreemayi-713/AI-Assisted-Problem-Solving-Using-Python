"""
Task 3: Translate Recursive Function (Python → C++)
This module contains a Python function that calculates factorial using recursion.
"""

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Call the function with different inputs to display results
if __name__ == "__main__":
    print(f"Input: 5 → Output: Factorial = {factorial(5)}")
    print(f"Input: 0 → Output: Factorial = {factorial(0)}")
