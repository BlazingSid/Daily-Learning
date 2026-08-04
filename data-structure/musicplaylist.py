playlist = []

while True:
    print("\n------ MUSIC PLAYLIST ------")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. Play Next Song")
    print("4. Show Playlist")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        song = input("Enter song name: ")
        playlist.append(song)
        print(song, "added to playlist.")

    elif choice == 2:
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            print("\nSongs:")
            for i in range(len(playlist)):
                print(i + 1, ".", playlist[i])

            index = int(input("Enter song number to remove: ")) - 1

            if 0 <= index < len(playlist):
                removed = playlist.pop(index)
                print(removed, "removed.")
            else:
                print("Invalid song number.")

    elif choice == 3:
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            playing = playlist.pop(0)
            print("Now Playing:", playing)

    elif choice == 4:
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            print("\nPlaylist:")
            for i in range(len(playlist)):
                print(i + 1, ".", playlist[i])

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")