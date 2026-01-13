# Exercise: Function for modular code
# Define functions to compute the area and perimeter of a rectangle.
# Date: 13 January 2026

def calculate_area(lenght, width):
    """Compute the area of rectangle."""
    return lenght * width

def calculate_perimeter(lenght, width):
    """Compute the perimeter of a rectangle."""
    return 2 * (lenght + width)

# Exemple usage
lenght = 5.0
width = 3.0

print("Rectangle dimensions:", lenght, "x", width)
print("Area:", calculate_area(lenght, width))
print("Perimeter:", calculate_perimeter(lenght, width))