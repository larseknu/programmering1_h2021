from album_8_7 import make_album

while True:
    artist = input("\nEnter album artist: ")
    title = input("Enter album title: ")

    print(make_album(artist, title))

    answer = input("\nDo you want to quit? Y/N ")

    if answer.upper() == "Y":
        exit()