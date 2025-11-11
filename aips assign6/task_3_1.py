def classify_age(age):
    if age < 0:
        print("Invalid age entered")
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 60:
        print("Adult")
    else:
        print("Senior Citizen")

# Input from user
age = int(input("Enter your age: "))
classify_age(age)
