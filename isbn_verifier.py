def is_valid(isbn):
    
    isbn = isbn.replace("-", "")

    if len(isbn) <= 9 or len(isbn) >= 11:
        return False
        
    total = 0
    
    for i, n in enumerate(isbn):
        if n.isdigit():
            total += int(n) * (10 - i)
        elif i == 9 and n is 'X':
            total += 10
        else:
            return False
    return total % 11 == 0
    
