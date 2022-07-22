def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')
    n = 0
    i = 1
    while n != number:
        i += 1
        if any(i % j == 0 for j in range(2, int(i**0.5) + 1)):
            continue
        n += 1
    return i    
