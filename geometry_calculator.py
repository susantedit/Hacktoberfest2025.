import math

# --- Rectangle Calculations ---

def rectangle_area(length, width):
  """Calculates the area of a rectangle."""
  if length <= 0 or width <= 0:
    return "Error: Length and width must be positive values."
  return length * width

def rectangle_perimeter(length, width):
  """Calculates the perimeter of a rectangle."""
  if length <= 0 or width <= 0:
    return "Error: Length and width must be positive values."
  return 2 * (length + width)

# --- Circle Calculations ---

def circle_area(radius):
  """Calculates the area of a circle."""
  if radius <= 0:
    return "Error: Radius must be a positive value."
  # Area = π * r^2
  return math.pi * (radius ** 2)

def circle_circumference(radius):
  """Calculates the circumference (perimeter) of a circle."""
  if radius <= 0:
    return "Error: Radius must be a positive value."
  # Circumference = 2 * π * r
  return 2 * math.pi * radius

# --- Square Calculations ---

def square_area(side):
  """Calculates the area of a square."""
  if side <= 0:
    return "Error: Side length must be a positive value."
  return side * side

def square_perimeter(side):
  """Calculates the perimeter of a square."""
  if side <= 0:
    return "Error: Side length must be a positive value."
  return 4 * side

# --- Example Usage ---

if __name__ == "__main__":
  # Rectangle example
  rect_l, rect_w = 10, 5
  print(f"Rectangle (L={rect_l}, W={rect_w}) Area: {rectangle_area(rect_l, rect_w)}")
  print(f"Rectangle (L={rect_l}, W={rect_w}) Perimeter: {rectangle_perimeter(rect_l, rect_w)}\n")

  # Circle example
  circ_r = 7
  print(f"Circle (R={circ_r}) Area: {circle_area(circ_r):.2f}") # Formatted to 2 decimal places
  print(f"Circle (R={circ_r}) Circumference: {circle_circumference(circ_r):.2f}\n")

  # Square example
  sq_s = 6
  print(f"Square (S={sq_s}) Area: {square_area(sq_s)}")
  print(f"Square (S={sq_s}) Perimeter: {square_perimeter(sq_s)}")
