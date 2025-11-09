def greet_user(name, gender=None):
    # Gender-neutral greeting
    if gender:
        gender = gender.lower()
        if gender == "male":
            title = "Mr."
        elif gender == "female":
            title = "Ms."
        else:
            title = "Mx."  # Inclusive title for non-binary or unspecified gender
    else:
        title = ""  # No title if gender not provided

    return f"Hello {title} {name}! Welcome."
    # Run the code with user input
if __name__ == "__main__":
    name = input("Enter your name: ")
    gender = input("Enter your gender (Male/Female/Other), or leave blank: ")
    gender = gender if gender.strip() else None
    print(greet_user(name, gender))
