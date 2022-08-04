def recite(start, take=1):
    lyrics = []
    for verse in range(start, start - take, -1):
        if start == 0:
            line = f"No more bottles of beer on the wall, no more bottles of beer."
        if start == 1:
            line = f"1 bottle of beer on the wall, 1 bottle of beer."
        if start >= 2:
            line = f"{start} bottles of beer on the wall, {start} bottles of beer."

        start = start - 1
        lyrics.append(line)

        if start == -1:
            line = f"Go to the store and buy some more, 99 bottles of beer on the wall."
        if start == 0:
            line = f"Take it down and pass it around, no more bottles of beer on the wall."
        if start == 1:
            line = f"Take one down and pass it around, 1 bottle of beer on the wall."
        if start >= 2:
            line = f"Take one down and pass it around, {start} bottles of beer on the wall."
        lyrics.append(line)
        lyrics.append("")
    lyrics = lyrics[:-1]

    return lyrics
