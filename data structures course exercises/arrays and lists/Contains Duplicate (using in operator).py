
def contains_duplicate(nums):
    seen = []
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.append(nums[i])
    return False

print(contains_duplicate([1,2,3,1]))