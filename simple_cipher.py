import random
from string import ascii_lowercase as lower
from itertools import cycle


class Cipher:
    def __init__(self, key=None):
        self.key = key
        if not self.key:
            self.key = "".join(random.choice(lower) for x in range(100))


    def encode(self, text):
        encoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            encoded.append(lower[(ord(ch1) % 97 + ord(ch2) % 97) % 26])
        return "".join(encoded)


    def decode(self, text):
        decoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            decoded.append(lower[(ord(ch1) % 97 - ord(ch2) % 97) % 26])
        return "".join(decoded)
      
