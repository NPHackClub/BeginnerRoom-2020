playlist = []

first_song = raw_input("Enter your first song: ")
playlist.append(first_song)

second_song = raw_input("Enter your second song: ")
playlist.append(second_song)

if second_song == first_song:
    print("Choose a different song: ")
    playlist.pop(1)
    second_song = raw_input("Enter your second song: ")
    playlist.append(second_song)

playlist.sort()

third_song = raw_input("Enter your third song: ")
playlist.append(third_song)

if third_song == second_song or third_song == first_song:
    print("Choose a different song: ")
    playlist.pop(2)
    third_song = raw_input("Enter your third song: ")
    playlist.append(third_song)

playlist.reverse()

print(playlist)