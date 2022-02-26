def abbreviate(words):
    phrase = words.upper().replace("-", " ").replace("_", " ").split()
    return "".join([letter[0]for letter in phrase])
