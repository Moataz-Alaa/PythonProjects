
def factorial(num):
    assert num == abs(num) and int(num) == num , 'Number must be positive integer'
    if num in [0, 1]:
        return 1
    return num * factorial(num - 1)