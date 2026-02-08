
def moveValue(array, value):
    average = 0.0
    if len(array) == 0:
        return array
    for i in range(len(array)):
        if array[i] == value:
            array.pop(i)
            array.append(value)
    return array

print(moveValue([1, 5, 3, 2, 3, 4, 1, 2, 5, 4, 4], 1))