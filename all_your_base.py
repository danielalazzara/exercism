def _split_number(n: int) -> list:
    n = str(n)
    return [int(i) for i in n]


def _rebase_to_decimal(input_base, digits):
    result = []
    for i, n in enumerate(digits[::-1]):
        result.append(n * (input_base ** i))
    return sum(result)


def _rebase_from_decimal(output_base, digits):
    result = []
    if all(d == 0 for d in str(digits)):
        return [0]
    if not isinstance(digits, int):
        n = int("".join(str(i) for i in digits))
    else:
        n = digits
    while n:
        result.append(int(n % output_base))
        n //= output_base
    return result[::-1]


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for d in digits:
        if not 0 <= d < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if all(d == 0 for d in digits):
        return [0]

    results = []

    if input_base == 10:
        _intermediate = digits
    else:
        _intermediate = _rebase_to_decimal(input_base, digits)

    if output_base == 10:
        return _split_number(_intermediate)
    else:
        return _rebase_from_decimal(output_base, _intermediate)
