
def get_diagonal(tup):
    diagonallist = []
    for i in range(len(tup)):
        diagonallist.append(tup[i][i])
    return tuple(diagonallist)

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)