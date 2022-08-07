def rectangles(strings):
    rectangle = 0
    for i in range(len(strings)):
        if '+' in strings[i]:
            for j in range(len(strings[i])):
                if strings[i][j] == '+':
                    for n in range(j + 1, len(strings[i])):
                        if strings[i][n] == '+':
                            for x in range(i + 1, len(strings)):
                                if strings[x][j] not in "+|" or strings[x][n] not in "+|":
                                    break
                                if strings[x][j] == "+" and strings[x][n] == "+":
                                    rectangle += 1
    return rectangle
    
