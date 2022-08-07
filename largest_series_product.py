import math


def largest_product(series, size):
    if not series and size == 0:
        return 1
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if size < 0: 
        raise ValueError("span must not be negative")
    if not series.isnumeric():
        raise ValueError("digits input must only contain digits")

    series = [int(i) for i in series]
    num = [series[i:i+size] for i in range(len(series) - size + 1)]

    return max([math.prod(i) for i in num])
