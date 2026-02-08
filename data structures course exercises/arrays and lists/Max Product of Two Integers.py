
def max_product(arr):
    maxproduct = arr[0]*arr[1]
    for i in range (0, len(arr)):
        for j in range (i+1, len(arr)):
            if arr[i]*arr[j] > maxproduct:
                maxproduct = arr[i]*arr[j]
    return maxproduct