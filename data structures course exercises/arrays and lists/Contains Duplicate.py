
def contains_duplicate(nums):
    seen = []
    for i in range(len(nums)):
        for j in range(len(seen)):
            if nums[i] == seen[j]:
                return True
        seen.append(nums[i])
    return False

print(contains_duplicate([1,2,3,1]))