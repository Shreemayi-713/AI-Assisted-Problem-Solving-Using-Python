# Function to calculate nth Fibonacci number using recursion
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of two previous Fibonacci numbers
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example
num = int(input("Enter a number: "))
print("Fibonacci number:", fibonacci(num))
