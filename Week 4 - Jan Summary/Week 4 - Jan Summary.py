import math

txt = "Find the area of either a rectangle, square, parallelogram, triangle, or trapezoid"
print(txt)

shape = input("Shape: ")

if shape == "rectangle" or shape == "Rectangle":
  l = float(input("Length: "))
  w = float(input("Width: "))
  print("The area of the rectangle is", l*w)
elif shape == "square" or shape == "Square":
  s = float(input("Side length: "))
  print("The area of the square is", s**2)
elif shape == "triangle" or shape == "Triangle":
  b = float(input("Base length: "))
  h = float(input("Height: "))
  print("The area of the triangle is", b*h/2)
elif shape == "parallelogram" or shape == "Parallelogram":
  b = float(input("Base length: "))
  h = float(input("Height: "))
  print("The area of the parallelogram is", b*h)
elif shape == "trapezoid" or shape == "Trapezoid":
  a = float(input("Length of A: "))
  b = float(input("Length of B: "))
  h = float(input("Height: "))
  print("The area of the trapezoid is", (a+b)*h/2)
elif shape == "circle" or shape == "Circle":
  r = float(input("Radius: "))
  print("The area of the circle is", round(r**2*math.pi, 2))
else:
  print("Choose to find the area of either a rectangle, square, parallelogram, triangle, or trapezoid.")