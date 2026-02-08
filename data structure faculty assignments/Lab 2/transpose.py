
def transpose(array):
    for i in range(len(array)):
            for j in range(i, len(array)):
                temp = array[i][j]
                array[i][j] = array[j][i]
                array[j][i] = temp
    return array

print(transpose([[1, 1], [2, 3]]))