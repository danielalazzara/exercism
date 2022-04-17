def sum_of_multiples(limit, multiples):
    result = set()
    for multiple in multiples:
        if multiple != 0:
            for x in range(multiple, limit, multiple):
                result.add(x) 
    return sum(result)
