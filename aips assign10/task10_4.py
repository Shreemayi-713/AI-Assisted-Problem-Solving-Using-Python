def calculate_average(scores):
    """Return the average of the scores."""
    return sum(scores) / len(scores)

def find_highest(scores):
    """Return the highest score."""
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest


def find_lowest(scores):
    """Return the lowest score."""
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    """Process and display score statistics using helper functions."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

# ---- User Input Section ----
scores = list(map(int, input("Enter scores separated by spaces: ").split()))
process_scores(scores)

