def cipher_text(plain_text):
	message = ''.join([t.lower() for t in plain_text if t.isalnum()])
	found = False
	c, r = (0,0)
	for c in range(len(message)):
		for r in range(len(message)):
			if (r * c) >= len(message) and c >= r and (c - r) <= 1 :
				found = True
				break
		if found:
			break

	if c == 0 and r == 0:
		return message
        
	char_list = [list(message[i*c:(i*c)+c].ljust(c)) for i in range(r)]
	transpose = [[char_list[j][i] for j in range(len(char_list))] for i in range(len(char_list[0]))]
	return ' '.join([''.join(lst) for lst in transpose])
