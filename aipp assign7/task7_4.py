class Rectangle:
    def __init__(self, length, width):  # Fixed: added 'self' parameter
        self.length = length
        self.width = width

# Take input from user
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Create Rectangle instance
rect = Rectangle(length, width)
print(f"Length: {rect.length}, Width: {rect.width}")

