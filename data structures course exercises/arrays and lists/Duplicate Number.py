
def remove_duplicates(arr):
    unique_arr = []
    for i in range(len(arr)):
        found = 0
        for j in range(len(unique_arr)):
            if arr[i] == unique_arr[j]:
                found = 1
                break
        if not found:
            unique_arr.append(arr[i])
    return unique_arr

testlist = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(testlist))