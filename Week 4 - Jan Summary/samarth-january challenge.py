# this is the VMSO-ify machine. Choose a 5 letter word (ex. kicad) and type in Mr. Jaimil Dalwadi's mark and let the machine do its wonders!

word = input("5 letter word: ")
w = (word[0])
o = (word[1])
r = (word[2])
d = (word[3])
s = (word[4])

import math
jaimil = int(input("jaimil's mark: "))
final = (jaimil - 1)

print(("because ")+(word)+(" changed to ")+(word.upper())+(" and is now ")+(w.upper())+(o.lower())+(r.upper())+(d.lower())+(s.upper())+(", your final mark is therefore a ")+str(final)+("%"))