num = int(input("Till what number do you want to end at: "))
i = 1

while i <= num:
  if (i%5 == 0) and (i%3 == 0):
    print("fizzbuzz")
    i += 1
  elif (i%3 == 0):
    print("fizz")
    i += 1
  elif (i%5 == 0):
    print("buzz")
    i += 1
  else:
    print(i)
    i += 1
else:
  print("done")