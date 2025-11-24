def bubble_sort(numbers):
    arr = numbers[:]  # work on a copy so we can show the original list later
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # list is already sorted
    return arr

def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


def main():
    user_input = input("Enter integers separated by spaces: ").strip()
    if not user_input:
        print("No numbers entered.")
        return

    try:
        numbers = [int(value) for value in user_input.split()]
    except ValueError:
        print("Please enter only integers.")
        return

    print(f"Original list: {numbers}")
    sorted_numbers = bubble_sort(numbers)
    print(f"Sorted list:   {sorted_numbers}")
    print(f"Is sorted:     {is_sorted(sorted_numbers)}")

if __name__ == "__main__":
    main()

