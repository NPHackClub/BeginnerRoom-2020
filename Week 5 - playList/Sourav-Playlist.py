user_input = input("Enter your first choice: ")
user_input2 = input("Enter your second choice: ")

playlist = [user_input, user_input2]
print(playlist)

playlist.sort()
print(playlist)

user_input3 = input("Enter your third choice: ")
playlist.append(user_input3)

playlist.reverse()
print(playlist)