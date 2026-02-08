
def productOfArray(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    element = arr.pop()
    return element * productOfArray(arr)

print(productOfArray([1,2,3,10]))