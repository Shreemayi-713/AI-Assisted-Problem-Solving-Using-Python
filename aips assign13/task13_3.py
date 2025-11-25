from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    """
    Represents a student with a name, age, and a collection of marks.
    """
    name: str
    age: int
    marks: List[int] = field(default_factory=list)

    def details(self) -> None:
        """
        Display the student's basic information in a readable form.
        """
        print(f"Name: {self.name} | Age: {self.age}")

    def total(self) -> int:
        """
        Calculate the total score across all stored marks.
        """
        return sum(self.marks)

def collect_student() -> Student:
    """
    Prompt the user for student details and return a populated Student object.
    """
    name = input("Enter student name: ").strip()
    age = int(input("Enter age: ").strip())
    marks = [
        int(input(f"Enter mark #{i + 1}: ").strip())
        for i in range(3)
    ]
    return Student(name=name, age=age, marks=marks)

def main() -> None:
    """
    Entry point for interacting with the Student class via user input.
    """
    student = collect_student()
    student.details()
    print(f"Total Marks: {student.total()}")


if __name__ == "__main__":
    main()
