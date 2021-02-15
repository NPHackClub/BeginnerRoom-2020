song1 = input("Insert your first song: ")
song2 = input("Insert your second song: ")
shuffle = [song1,song2]
shuffle.sort()
song3 = input("Insert your third song: ")
shuffle.insert(0,song3)
print(shuffle)
