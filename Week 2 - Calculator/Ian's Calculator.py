import math
print("this calculator will only work with whole number inputs")
print("choose an equasion from the following")
i = input("pythagoras theorem, area of a square, or perimeter of a triangle: ") 

if i == "pythagoras theorem":
	print("you selected the pythagoras theorem calculator")
	a = input("enter the value of side a: ")
	b = input("enter the value of side b: ")
	#a^2
	a = int(a)
	a = a*a
	#b^2
	b = int(b)
	b = b*b
	
	ans = a+b
	ans = math.sqrt(ans)
	print("the answer is")
	print(ans)

if i == "area of a square":
	print("you selected the area of a square calculator")
	a = input("enter the value of side a: ")
	b = input("enter the value of side b: ")

	a = int(a)
	b = int(b)

	ans = a*b
	print("the answer is")
	print(ans)

if i == "perimeter of a triangle":
	print("you selected the perimeter of a triangle calculator")
	a = input("enter the value of side a: ")
	b = input("enter the value of side b: ")
	c = input("enter the value of side c: ")

	a = int(a)
	b = int(b)
	c = int(c)

	ans = a+b+c
	print("the answer is")
	print(ans)
