output = ''

while True:
  n = str(input('Write Letter: '))
  n = n.lower()
  for character in n:
    number = ord(character) - 96
    output = number
  if output < 0:
    print("Invalid input! Enter a letter")
    continue
  break

if str(output) == "1":
  output = "1st"
  print("This is the",output, "letter of the alphabet")
elif str(output) == "2":
  output = "2nd"
  print("This is the",output, "letter of the alphabet")
elif str(output) == "3":
  output = "3rd"
  print("This is the",output, "letter of the alphabet")
else:
  print("This is the ",output, "th letter of the alphabet", sep='')