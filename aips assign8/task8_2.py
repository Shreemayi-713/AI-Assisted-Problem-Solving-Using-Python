def assign_grade(score):
    """Return grade based on the score."""
    if not isinstance(score, (int, float)):
        return "Invalid"

    if score < 0 or score > 100:
        return "Invalid"

    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


# ------------------------------------------
# USER INPUT
# ------------------------------------------
try:
    user_score = float(input("Enter the score: "))
    print("Grade:", assign_grade(user_score))
except ValueError:
    print("Invalid input! Please enter a number.")


# ------------------------------------------
# TEST CASES
# ------------------------------------------
test_cases = {
    "Boundary A Lower": (90, "A"),
    "A Upper": (100, "A"),
    "Boundary B Lower": (80, "B"),
    "B Upper": (89, "B"),
    "Boundary C Lower": (70, "C"),
    "C Upper": (79, "C"),
    "Boundary D Lower": (60, "D"),
    "D Upper": (69, "D"),
    "Boundary F Upper (59)": (59, "F"),

    # Invalid values
    "Negative Score": (-5, "Invalid"),
    "Above 100": (105, "Invalid"),
    "String Input": ("eighty", "Invalid"),
    "None Input": (None, "Invalid"),
    "Float Valid": (85.5, "B"),
    "Float Invalid (>100)": (150.8, "Invalid")
}

# ------------------------------------------
# TEST RUNNER
# ------------------------------------------
print("\nRunning Test Cases:\n")
for name, (input_value, expected_output) in test_cases.items():
    result = assign_grade(input_value)
    status = "PASS" if result == expected_output else "FAIL"
    print(f"{name}: Input={input_value}, Expected={expected_output}, Got={result} --> {status}")
