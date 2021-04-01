Ahmad = int(input('what number shall we end at? '))
i = 1
j = 0
k = 0

while i != Ahmad + 1:
  j = i % 3
  if j == 0:
    print('fizz')
  k = i % 5
  if k == 0:
    print('buzz')
  if j != 0:
    if k != 0:
      print(i)
  i += 1
print("done")