def primes(limit):
    prime_numbers = set(range(2, limit+1))
    for n in range(2, limit+1):
        if n in prime_numbers:           
            prime_numbers -= set(range(2*n, limit+1, n))

    return list(prime_numbers)
  
