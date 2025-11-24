def linear_search(values, target):
    """Return index of target in values or -1 if not found."""
    for idx, value in enumerate(values):
        if value == target:
            return idx
    return -1


def main():
    raw_values = input("Enter numbers separated by spaces: ").strip()
    values = [int(token) for token in raw_values.split()] if raw_values else []
    target = int(input("Enter the number to search for: ").strip())

    index = linear_search(values, target)
    if index == -1:
        print(f"{target} not found in the list.")
    else:
        print(f"{target} found at index {index}.")


if __name__ == "__main__":
    main()

