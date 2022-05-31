def is_armstrong_number(number):
    n = len(str(number))
    total = 0
    
    for digit in str(number):
        total = total + (int(digit) ** n) 
    return total == number
    
