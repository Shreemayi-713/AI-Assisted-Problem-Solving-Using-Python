"""
Task 4: Data Structures with Functions (JavaScript → Python)
This module contains a Python function that prints student names from a list.
"""

def print_students(students):
    """Print each student name from the provided list."""
    print("Student List:")
    for name in students:
        print(name)


if __name__ == "__main__":
    students = ['Alice', 'Bob', 'Charlie']
    print_students(students)
