song1 = input("Insert your first song: ")
song2 = input("Insert your second song: ")
shuffle = [song1, song2]
shuffle.sort()
song3 = input("Insert your third song: ")
shuffle.append(song3)
shuffle.reverse()
print(shuffle)
