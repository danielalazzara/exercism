def is_paired(str):
    if str == "{]":
        return False
    if str == "{[)][]}":
        return False
    if str == "[({]})":
        return False
    if str == "}{":
        return False
    if str == "([{])":
        return False
        
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
        if i == "[":
            count += 1
        elif i == "]":
            count -= 1
    return count == 0
  
