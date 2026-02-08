
def power(base, exponent):
    assert exponent == abs(exponent) and int(exponent) == exponent , 'Exponent must be positive integer'
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)