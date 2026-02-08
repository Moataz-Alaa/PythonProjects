
def reverse(arr):
    if len(arr) == 0:
        return []
    first = 0
    last = len(arr) - 1
    for i in range(len(arr)):
        if first >= last:
            return arr
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp
        first += 1
        last -= 1

print(reverse([16, 12, 15, 12, 11, 15, 12, 16, 11, 16]))