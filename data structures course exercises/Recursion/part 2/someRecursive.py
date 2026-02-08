
# I solved this problem without knowing what is a callback LOL

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return None
    if cb(arr[0]):
        return True
    if len(arr) == 1:
        return False
    return someRecursive(arr[1:], cb)

print(someRecursive([1,2,3,4], isOdd)) # true
print(someRecursive([4,6,8,9], isOdd)) # true
print(someRecursive([4,6,8], isOdd)) # false