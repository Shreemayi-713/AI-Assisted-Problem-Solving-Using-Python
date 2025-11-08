from palindrome import is_palindrome
from typing import Iterable

#!/usr/bin/env python3
"""
palindrome.py

Provides a simple, efficient palindrome-checking function.

Usage:
    is_palindrome("A man, a plan, a canal: Panama")  # True
"""



def _normalize(s: str, ignore_case: bool, ignore_non_alnum: bool) -> str:
    if ignore_non_alnum:
        if ignore_case:
            return "".join(ch.lower() for ch in s if ch.isalnum())
        return "".join(ch for ch in s if ch.isalnum())
    return s.lower() if ignore_case else s


def is_palindrome(value, *, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool:
    """
    Return True if `value` is a palindrome.

    Parameters:
    - value: str or any iterable that yields characters (will be converted to str if not).
    - ignore_case: when True, 'A' and 'a' are considered equal (default True).
    - ignore_non_alnum: when True, non-alphanumeric characters are ignored (default True).

    Examples:
    - is_palindrome("Racecar") -> True
    - is_palindrome("No lemon, no melon") -> True
    - is_palindrome("12321") -> True
    """
    if value is None:
        return False

    s = value if isinstance(value, str) else str(value)
    s = _normalize(s, ignore_case, ignore_non_alnum)

    # Two-pointer check (O(n) time, O(1) extra space)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    tests = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "No lemon, no melon",
        "hello",
        12321,
        12345,
        "",
        None,
    ]
    for t in tests:
        print(f"{repr(t):30} -> {is_palindrome(t)}")