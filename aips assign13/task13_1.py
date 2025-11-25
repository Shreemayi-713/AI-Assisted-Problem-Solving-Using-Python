from math import pi

def rectangle_area(length: float, width: float) -> float:
    """Return area of a rectangle."""
    return length * width

def square_area(side: float) -> float:
    """Return area of a square."""
    return side * side

def circle_area(radius: float) -> float:
    """Return area of a circle."""
    return pi * radius * radius

SHAPE_CONFIG = {
    "rectangle": {"func": rectangle_area, "dimensions": ("length", "width")},
    "square": {"func": square_area, "dimensions": ("side",)},
    "circle": {"func": circle_area, "dimensions": ("radius",)},
}

def calculate_area(shape: str, *dimensions: float) -> float:
    """Calculate area for a supported shape."""
    shape_key = shape.lower()
    if shape_key not in SHAPE_CONFIG:
        raise ValueError(f"Unsupported shape: {shape}")

    config = SHAPE_CONFIG[shape_key]
    expected = len(config["dimensions"])
    if len(dimensions) != expected:
        raise ValueError(f"{shape.title()} needs {expected} dimensions.")

    return config["func"](*dimensions)

def prompt_user_for_area() -> None:
    """Gather user input and print the calculated area."""
    shape = input("Enter shape (rectangle/square/circle): ").strip().lower()
    if shape not in SHAPE_CONFIG:
        print(f"Unsupported shape: {shape}")
        return

    dimensions = []
    for label in SHAPE_CONFIG[shape]["dimensions"]:
        while True:
            try:
                value = float(input(f"Enter {label}: "))
                if value <= 0:
                    raise ValueError
            except ValueError:
                print("Please enter a positive number.")
                continue
            dimensions.append(value)
            break

    area = calculate_area(shape, *dimensions)
    print(f"The area of the {shape} is {area:.2f}")



if __name__ == "__main__":
    prompt_user_for_area()

