def rotate(text, key): 
    cipherText = []
    for ch in text:
        if not ch.isalpha():
            cipherText.append(ch)
            continue

        ord_a = ord('a') if ch.islower() else ord('A')
        final_letter = ord(ch) - ord_a
        stay_in_alphabet = (final_letter + key) % 26
        cipherText.append(chr(ord_a + stay_in_alphabet))
    return ''.join(cipherText)
    
