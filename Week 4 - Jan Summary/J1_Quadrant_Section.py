#python J1_Quadrant_Section.py
import math
x = int(input("Coordinate X: "))
y = int(input("Coordinate Y: "))

if (x > 0) and (y > 0):
  print("1")
if (x < 0) and (y > 0):
    print ("2")
if (x < 0) and (y < 0):
    print ("3")
if (x > 0) and (y < 0):
    print ("4")