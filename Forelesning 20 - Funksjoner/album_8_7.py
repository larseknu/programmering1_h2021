def make_album(artist, title, tracks=0):
    album = {"artist": artist, "title": title}

    if tracks:
        album["tracks"] = tracks

    return album

if __name__ == "__main__":
    hans_zimmer_album = make_album("Hans Zimmer", "Interstellar", 10)
    print(hans_zimmer_album)

    print(make_album("Panic at the Disco", "A fever you can't sweat out", 13))
    print(make_album("Bo Burnham", "The water is fine"))
    print(make_album("Philter", "The Beautiful Lies"))
