
def common_elements(tuple1, tuple2):
    commonlist = []
    for i in tuple1:
        if i in tuple2:
            commonlist.append(i)
    return tuple(commonlist)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)