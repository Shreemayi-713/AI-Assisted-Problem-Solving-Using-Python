def grade(score: float) -> str:
    """Return the letter grade corresponding to the numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def main() -> None:
    try:
        score = float(input("Enter the score (0-100): "))
    except ValueError:
        print("Invalid score. Please enter a numeric value.")
        return

    print(f"Grade: {grade(score)}")


if __name__ == "__main__":
    main()

