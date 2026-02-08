
def reverse_dict(my_dict):
    reverseddict = {}
    for key, value in my_dict.items():
        reverseddict[value] = key
    return reverseddict

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))