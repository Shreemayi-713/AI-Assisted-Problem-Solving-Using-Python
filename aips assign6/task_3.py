def classify_age(age):
    if age >= 0:
        if age < 13:
            print("Child")
        elif age >= 13 and age < 20:
            print("Teenager")
        elif age >= 20 and age < 60:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Invalid age entered")

# Input from user
age = int(input("Enter your age: "))
classify_age(age)
