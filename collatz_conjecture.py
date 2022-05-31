def steps(number):
    final = 0
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")  
    while number > 1:
        number = 3 * number + 1 if number % 2 else number / 2
        final += 1
    return final
    
