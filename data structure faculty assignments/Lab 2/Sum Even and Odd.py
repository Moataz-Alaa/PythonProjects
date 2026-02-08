
def sumEvenOdd(array):
    SEven_SOdd = [0, 0]
    if len(array) == 0:
        return SEven_SOdd
    for i in range(len(array)):
        if array[i] % 2 == 0:
            SEven_SOdd[0] += array[i]
        else:
            SEven_SOdd[1] += array[i]
    return SEven_SOdd
