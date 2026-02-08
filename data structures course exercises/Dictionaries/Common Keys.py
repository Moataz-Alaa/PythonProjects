def merge_dicts(dict1, dict2):
    mergeddict = dict1.copy()
    for key in dict2:
        if key in mergeddict:
            mergeddict[key] += dict2[key]
        else:
            mergeddict[key] = dict2[key]
    return mergeddict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))