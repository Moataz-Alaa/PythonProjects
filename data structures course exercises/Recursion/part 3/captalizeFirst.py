
def capitalizeFirstString(strng):
    if len(strng) == 1:
        return strng.capitalize()
    return capitalizeFirstString(strng[:len(strng)-1]) + strng[len(strng)-1]

def capitalizeFirst(arr):
    if len(arr) == 1:
        return [capitalizeFirstString(arr[len(arr)-1])]
    capitalizeFirst(arr[:len(arr)-1]).append(capitalizeFirstString(arr[len(arr)-1]))

# using iteration is far easier here...

def capitalizeFirstItr(arr):
    for i in range(len(arr)):
        arr[i] = capitalizeFirstString(arr[i])
    return arr

print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']