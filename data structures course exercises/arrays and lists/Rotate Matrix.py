def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(len(matrix)):
         matrix[i].reverse()
    return matrix

testmatrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(testmatrix))