#input
y=mx = input("4 Letter word ")
word = []
beta = ''

#processing
beta = y=mx[0].upper()
word.append(beta)

beta = y=mx[1].lower()
word.append(beta)

beta = y=mx[2].upper()
word.append(beta)

beta = y=mx[3].lower()
word.append(beta)

word = ''.join(word)

#output
print(word)