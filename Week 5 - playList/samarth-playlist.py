print("Your Katsurap Playlist")
songs = []
def first_song():
    first = (input("add your first song, yo!: "))
    songs.append(first)

first_song()

def second_song():
    second = (input("add your second song, yo!: "))
    second_check = songs.count(second)
    if second_check > 0:
        print ("you can't put the same song again, yo!")
        return second_song()
    else:
        songs.append(second)
        songs.sort()

second_song()

def third_song():
    third = (input("add your third song, yo!: "))
    third_check = songs.count(third)
    if third_check > 0:
        print("you can't put the same song again, yo!")
        return third_song()
    else:
        songs.append(third)
        songs.reverse()
        print("your Katsurap approved playlist, yo!: " + str(songs))

third_song()