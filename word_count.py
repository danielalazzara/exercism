from collections import Counter
import re

def count_words(sentence):
    return Counter(re.findall(r"[0-9a-z]+(?:'[a-z]+)?", sentence.lower()))
