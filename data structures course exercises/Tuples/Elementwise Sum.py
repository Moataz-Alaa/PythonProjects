
def tuple_elementwise_sum(tuple1, tuple2):
    sumlist = []
    for i in range(len(tuple1)):
        sumlist.append(tuple1[i] + tuple2[i])
    return tuple(sumlist)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)