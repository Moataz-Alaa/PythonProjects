
def insert_value_front(input_tuple, value_to_insert):
    input_list = list(input_tuple)
    input_list.insert(0, value_to_insert)
    return tuple(input_list)

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)