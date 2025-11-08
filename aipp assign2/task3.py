import math

def area_circle(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2

def area_rectangle(length, width):
    """Calculate area of a rectangle."""
    return length * width

def area_triangle(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

def area_square(side):
    """Calculate area of a square."""
    return side ** 2

def area_trapezoid(base1, base2, height):
    """Calculate area of a trapezoid."""
    return 0.5 * (base1 + base2) * height

if __name__ == "__main__":
    # Test all functions with example values
    print("Area Calculations:")
    print(f"Circle (radius=5): {area_circle(5):.2f}")
    print(f"Rectangle (length=4, width=6): {area_rectangle(4, 6)}")
    print(f"Triangle (base=3, height=4): {area_triangle(3, 4)}")
    print(f"Square (side=5): {area_square(5)}")
    print(f"Trapezoid (base1=3, base2=5, height=4): {area_trapezoid(3, 5, 4)}")