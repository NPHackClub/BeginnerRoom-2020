import math

x = input("Which side are you trying to find? ")

if x == "c" or x == "c":
    a = int(input("Side a: "))
    b = int(input("Side b: "))
    c = math.sqrt(a**2+b**2)
    print("The length of side c is", round(c,2))
elif x == "b" or x == "B":
    a = int(input("Side a: "))
    c = int(input("Side c: "))
    b = math.sqrt(c**2-a**2)
    print("The length of side b is", round(b,2))
elif x == "a" or x == "A":
    b = int(input("Side b: "))
    c = int(input("Side c: "))
    a = math.sqrt(c**2-b**2)
    print("The length of side a is", round(a,2))
else:
    print("Please select a side between a, b, or c")