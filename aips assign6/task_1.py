class Student:
    def __init__(self, name, roll_no, age, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks
        self.grade = grade

    def display_details(self):
        print("\n--- Student Details ---")
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Grade:", self.grade)


# Taking input from the user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
grade = input("Enter grade: ")

# Creating object and displaying details
student1 = Student(name, roll_no, age, marks, grade)
student1.display_details()
