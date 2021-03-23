n = int(input('numero: '))
print('multiplication table of', n)
x = 1
y = 0
z = 0

for ahmad in range(10):
  print(n*x)
  x += 1

print('sum of all numbers until', n)

for i in range(0, n):
  y += 1
  z += y
print(z)