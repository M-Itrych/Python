def twoSum(nums, target):
    prevMap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[num] = i
    return