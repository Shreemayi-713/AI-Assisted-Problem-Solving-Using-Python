# Job Applicant Scoring System

def applicant_score(name, gender, experience, education_level, skills):
    print(f"\nApplicant: {name} ({gender})")

    score = 0
    if experience >= 5:
        score += 3
    elif experience >= 2:
        score += 2
    else:
        score += 1

    if education_level.lower() in ["masters", "phd"]:
        score += 3
    elif education_level.lower() == "bachelors":
        score += 2
    else:
        score += 1

    if skills >= 5:
        score += 3
    elif skills >= 3:
        score += 2
    else:
        score += 1

    print(f"Total Score: {score}")
    if score >= 8:
        print("Highly Suitable ✅")
    elif score >= 5:
        print("Moderately Suitable ⚙️")
    else:
        print("Not Suitable ❌")

# Example input
name = input("Enter applicant name: ")
gender = input("Enter gender (Male/Female/Other): ")
experience = int(input("Enter years of experience: "))
education_level = input("Enter education level (Highschool/Bachelors/Masters/PhD): ")
skills = int(input("Enter number of relevant skills: "))

applicant_score(name, gender, experience, education_level, skills)
