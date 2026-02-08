from array import *

def missing_number(arr, n):
    measuredsum = 0
    actualsum = (n*(n+1))/2
    for i in range(0, len(arr)):
        measuredsum += arr[i]
    return int(actualsum - measuredsum)

arr1 = array('i',[1,2,3,5])

print(missing_number(arr1, 5))