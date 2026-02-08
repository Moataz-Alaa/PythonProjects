def max_value_key(my_dict):
    for key in my_dict:
        if my_dict[key] == max(my_dict.values()):
            return key


my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))