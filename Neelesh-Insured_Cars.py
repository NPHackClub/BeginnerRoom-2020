#I made two, one was like the example and the other one was using dictionaries.
#python Neelesh-Insured_Cars.py
nphc = []

a = raw_input('Enter car #1 owner name: ')
nphc.append(a)

b = raw_input('Enter car #1 brand name: ')
nphc.append(b)

c = raw_input('Enter car #1 model: ')
nphc.append(c)

a1 = raw_input('Enter car #2 owner name: ')
nphc.append(a1)

b1 = raw_input('Enter car #2 brand name: ')
nphc.append(b1)

c1 = raw_input('Enter car #2 model: ')
nphc.append(c1)

a2 = raw_input('Enter car #3 owner name: ')
nphc.append(a2)

b2 = raw_input('Enter car #3 brand name: ')
nphc.append(b2)

c2 = raw_input('Enter car #3 model: ')
nphc.append(c2)

print(' ')

print('________________Vehicles Insured________________')
print ((a) + ' owns a ' + (b) + ' ' + (c) + '.')
print ((a1) + ' owns a ' + (b1) + ' ' + (c1) + '.')
print ((a2) + ' owns a ' + (b2) + ' ' + (c2) + '.')

print('________________________________________________')

print(' ')

print(' ')


print('________________Vehicles Insured________________')
np_hackclub = {'Enter car #1 owner name' : 'Sam',
               'Enter car #1 brand name' : 'Porche',
               'Enter car #1 model' : 'Taycan.'
}
np_hackclub.update({'Enter car #1 brand name' : 'Porche'})

np_hackclub.update({'Enter car #1 model' : 'Taycan'})

np_hackclub.update({'Enter car #2 owner name' : 'Ayush'})

np_hackclub.update({'Enter car #2 brand name' : 'Tesla'})

np_hackclub.update({'Enter car #2 model' : 'Roadster Plaid.'})

np_hackclub.update({'Enter car #3 owner name' : 'Jaimil.'})

np_hackclub.update({'Enter car #3 brand name' : 'McLaren.'})

np_hackclub.update({'Enter car #3 model' : '720 S.'})
print (np_hackclub)
print('________________________________________________')

print(' ')