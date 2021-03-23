#User input and statement
n = int(input("Enter number: "))
print("multiplication table of", n)

#Multiplication of n to 10
for x in range(1,11):
  print(n*x)

#Sum of all numbers until n and statement
print("sum of all numbers until", n)
total = 0
for y in range(n+1):
  total += y
else:
  print(total)