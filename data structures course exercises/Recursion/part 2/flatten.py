
def flatten(arr):
    result = []
    for thing in arr:
        if type(thing) is list:
            result.extend(flatten(thing)) #as long as the thing is an array I will extend its "flatten" result to the previous result
            #Eventually, one of them will return a one dimentional array
        else:
            result.append(thing)
    return result

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]