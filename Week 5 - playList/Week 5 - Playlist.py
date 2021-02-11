song1 = input("Enter your first choice: ")
song2 = input("Enter your second choice: ")

if song1 == song2:
  print("You already entered that choice")
  song2 = input("Enter your second choice: ")

song3 = input("Enter your third choice: ")

if song2 == song3 or song1 == song3:
  print("You already entered that choice")
  song3 = input("Enter your third choice: ")

playlist = [song1, song2]

playlist.sort()
playlist.insert(2, song3)
playlist.reverse()
print(playlist)