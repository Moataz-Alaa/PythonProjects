
def array_average(arr):
    average = 0.0
    if len(arr) == 0:
        return average
    for i in range(len(arr)):
        average += arr[i]
    average = average / len(arr)
    return average
