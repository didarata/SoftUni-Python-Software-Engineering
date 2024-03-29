def add_songs(*typles):
    songs = {}

    for t in typles:
        song, lyrics = t

        if song not in songs:
            songs[song] = []

        songs[song].extend(lyrics)

    output= []

    for s_title, s_lyrics in songs.items():
        output.append("- " + s_title)
        output.extend(s_lyrics)

    return "\n".join(output)

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))