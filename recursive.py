# Recursive and iterative factorial implementations


def factorial_recursive(n: int) -> int:
    """Recursive factorial.

    # Function: recursive factorial
    # Input: n (int) -- must be >= 0
    # Output: n! as int
    # Edge cases: 0! == 1

    Raises TypeError for non-int inputs and ValueError for negative integers.
    """
    if not isinstance(n, int):
        raise TypeError("factorial_recursive: input must be an int")
    if n < 0:
        raise ValueError("factorial_recursive: input must be >= 0")
    if n == 0:
        return 1
    # recursive step: n * (n-1)!
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Iterative factorial.

    # Function: iterative factorial
    # Input: n (int) -- must be >= 0
    # Output: n! as int
    # Edge cases: 0! == 1

    Uses a simple loop to compute the product from 1..n.
    """
    if not isinstance(n, int):
        raise TypeError("factorial_iterative: input must be an int")
    if n < 0:
        raise ValueError("factorial_iterative: input must be >= 0")

    result = 1
    # loop from 2 to n multiplying into result
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # quick demo
    samples = [0, 1, 5, 10]
    for s in samples:
        print(f"{s}! recursive = {factorial_recursive(s)}; iterative = {factorial_iterative(s)}")
