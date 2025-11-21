def divide_numbers(dividend: float, divisor: float) -> float:
    """
    Divide two numbers with robust error handling.

    The function validates the divisor to prevent ZeroDivisionError and raises
    a ValueError with a clear message if division by zero is attempted.
    """
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return dividend / divisor

def main() -> None:
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        result = divide_numbers(dividend, divisor)
    except ValueError as exc:
        print(f"Error: {exc}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()


