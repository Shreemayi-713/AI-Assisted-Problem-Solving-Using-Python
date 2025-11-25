from typing import List

def compute_squares(values: List[int]) -> List[int]:
    """Return the square of each integer using a list comprehension."""
    return [value * value for value in values]

def parse_numbers(raw: str) -> List[int]:
    """
    Convert a whitespace separated string of integers into a list.

    Raises:
        ValueError: If any token cannot be converted to an integer.
    """
    if not raw.strip():
        raise ValueError("Please enter at least one number.")
    return [int(token) for token in raw.split()]

def main() -> None:
    """
    Prompt for numbers, show the computed squares, and narrate the refactor.
    """
    print("Task 13.4 – Inefficient Loop Refactoring")
    user_input = input("Enter integers separated by spaces: ")
    try:
        numbers = parse_numbers(user_input)
    except ValueError as err:
        print(f"Invalid input: {err}")
        return

    squares = compute_squares(numbers)
    print("AI suggested using a list comprehension for squaring numbers.")
    print(f"Input numbers: {numbers}")
    print(f"Squared values: {squares}")


if __name__ == "__main__":
    main()
