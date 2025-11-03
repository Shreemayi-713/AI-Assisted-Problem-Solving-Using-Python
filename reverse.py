# Function to reverse a string
def reverse_string(s: str) -> str:
    """Return the reverse of the input string.

    Example:
        reverse_string('abc') -> 'cba'
    """
    return s[::-1]


if __name__ == '__main__':
    # quick demo
    print(reverse_string('hello'))
    print(reverse_string('AIPS'))
    print(reverse_string('python'))
    print(reverse_string('AI'))



