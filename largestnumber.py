"""Utilities to find the largest number in a list.

Provides a simple, efficient single-pass implementation and a small CLI demo.
"""
from typing import Iterable, Optional


def largest_number(values: Iterable[float]) -> float:
    """Return the largest number from an iterable of numbers.

    Args:
        values: An iterable of numeric values (ints or floats).

    Returns:
        The largest numeric value.

    Raises:
        ValueError: If `values` is empty.
        TypeError: If an element is not comparable to the current max.

    Complexity: O(n) time, O(1) extra space.

    This function mirrors the behaviour of Python's built-in `max` for
    numeric inputs but uses an explicit single-pass loop to make the
    algorithm clear and easy to test.
    """
    iterator = iter(values)
    try:
        current_max = next(iterator)
    except StopIteration:
        raise ValueError("largest_number() arg is an empty iterable")

    for v in iterator:
        # rely on Python's comparison; a TypeError will be raised if
        # the values are not mutually comparable (e.g., int vs str)
        if v > current_max:
            current_max = v

    return current_max


if __name__ == "__main__":
    import sys

    # If numbers are not provided as CLI args, prompt the user interactively
    if len(sys.argv) <= 1:
        raw = input("Enter numbers separated by spaces or commas: ").strip()
        parts = [p for chunk in raw.split() for p in chunk.split(",") if p]
    else:
        parts = sys.argv[1:]

    # Parse inputs to floats
    try:
        nums = [float(x) for x in parts]
    except ValueError:
        print("All inputs must be numbers.")
        sys.exit(1)

    print(f"Largest: {largest_number(nums)}")
