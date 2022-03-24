def factors(value):
    result = []
    first = 2

    while value >= 2:
        if value % first == 0:
            result.append(first)
            value = value / first
        else:
            first = first + 1
    return result
