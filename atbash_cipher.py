plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    encoded = ''
    for i in plain_text:
        if i.isalpha():
            encoded += cipher[plain.index(i.lower())]
        elif i.isdigit():
            encoded += i
    final = ''
    for i in range(len(encoded)):
        final += encoded[i] + " " if (i + 1) % 5 == 0 else encoded[i]
    return final.strip()


def decode(ciphered_text):
    decoded = ''
    for i in ciphered_text:
        if i.isalpha():
            decoded += plain[cipher.index(i)]
        elif i.isdigit():
            decoded += i
    return decoded 
