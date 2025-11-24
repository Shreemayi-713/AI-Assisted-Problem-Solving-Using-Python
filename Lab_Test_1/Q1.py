import timeit


def reverse_manual(user_list):
    """Reverse a list by iterating from the end to the start."""
    result = []
    for index in range(len(user_list) - 1, -1, -1):
        result.append(user_list[index])
    return result


def reverse_slice(user_list):
    """Reverse a list using slicing."""
    return user_list[::-1]


def reverse_reversed_builtin(user_list):
    """Reverse a list via the built-in reversed() iterator."""
    return list(reversed(user_list))


def reverse_recursive(user_list):
    """Reverse a list recursively."""
    if len(user_list) <= 1:
        return user_list[:]
    return user_list[-1:] + reverse_recursive(user_list[:-1])


def parse_user_input(raw_input):
    """Convert user input into a list, parsing integers when possible."""
    items = raw_input.split()
    parsed = []
    for item in items:
        try:
            parsed.append(int(item))
        except ValueError:
            parsed.append(item)
    return parsed


def benchmark(function_map, data, iterations=1000):
    """Return timing results for each reversal implementation."""
    results = {}
    for name, func in function_map.items():
        timer = timeit.Timer(lambda f=func: f(list(data)))
        results[name] = timer.timeit(number=iterations)
    return results


def main():
    raw = input("Enter list elements separated by spaces: ").strip()
    user_list = parse_user_input(raw)

    if not user_list:
        print("No input provided. Using default data: 1 2 3 4 5.")
        user_list = [1, 2, 3, 4, 5]

    implementations = {
        "Manual loop": reverse_manual,
        "Slicing": reverse_slice,
        "Built-in reversed()": reverse_reversed_builtin,
        "Recursion": reverse_recursive,
    }

    print("\nReversal results:")
    for name, func in implementations.items():
        print(f"{name:>20}: {func(user_list)}")

    # Prepare benchmark data without exceeding recursion depth
    base_data = user_list or [1, 2, 3, 4, 5]
    repeat_factor = min(50, max(1, 500 // len(base_data)))
    benchmark_data = (base_data * repeat_factor)[:500]

    timings = benchmark(implementations, benchmark_data, iterations=2000)

    print("\nPerformance (seconds over 2000 iterations):")
    fastest = min(timings, key=timings.get)
    for name, duration in timings.items():
        print(f"{name:>20}: {duration:.6f}s")
    print(f"\nFastest implementation: {fastest}")


if __name__ == "__main__":
    main()
