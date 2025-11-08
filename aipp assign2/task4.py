def sum_of_squares_two_numbers(num1, num2):
    
    return (num1 ** 2) + (num2 ** 2)


if __name__ == "__main__":
    print("=" * 50)
    print("Sum of Squares of Two Numbers")
    print("=" * 50)
    
    # Get input from user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculate sum of squares
        result = sum_of_squares_two_numbers(num1, num2)
        
        # Display result
        print(f"\nResult: {num1}² + {num2}² = {num1**2} + {num2**2} = {result}")
        print(f"Sum of squares: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

