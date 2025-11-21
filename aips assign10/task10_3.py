class Employee:
    """Represents an employee with a name and salary."""

    def __init__(self, name, salary):
        """Initialize employee details."""
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        """Increase the employee's salary by a given percentage."""
        self.salary += self.salary * percent / 100

    def display_info(self):
        """Display formatted employee information."""
        print(f"Employee Name: {self.name}")
        print(f"Current Salary: {self.salary:.2f}")
        
# ---- User Input Section ----
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
percent = float(input("Enter percentage increase: "))

emp = Employee(name, salary)
emp.increase_salary(percent)

print("\n--- Employee Details ---")
emp.display_info()
