# Loan Approval System with User Input

def loan_approval(name, gender, age, income, credit_score, existing_loans):
    print(f"\nApplicant: {name} ({gender})")

    score = 0
    if income > 40000:
        score += 2
    if credit_score > 700:
        score += 3
    if existing_loans < 2:
        score += 1
    if 21 <= age <= 60:
        score += 1

    # Decision
    if score >= 6:
        print("Loan Approved ✅")
    elif 4 <= score < 6:
        print("Loan Approved with Conditions ⚠️")
    else:
        print("Loan Denied ❌")


# Taking user input
name = input("Enter applicant name: ")
gender = input("Enter gender (Male/Female/Other): ")
age = int(input("Enter age: "))
income = float(input("Enter annual income: "))
credit_score = int(input("Enter credit score: "))
existing_loans = int(input("Enter number of existing loans: "))

loan_approval(name, gender, age, income, credit_score, existing_loans)
