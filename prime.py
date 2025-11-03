def is_prime(n: int) -> bool:
    """Return True if n is prime, otherwise False.

    Raises:
        TypeError: if n is not an int.
    """
    if not isinstance(n, int):
        raise TypeError("is_prime: input must be an int")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    import sys
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print(f"{n} is prime" if is_prime(n) else f"{n} is not prime")