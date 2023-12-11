#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

def maxproduct(nums):
    max_product = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] - 1) * (nums[j] - 1) > max_product and i != j:
                max_product = (nums[i] - 1) * (nums[j] - 1)
    return max_product


inpu = [3,4,5,2]
print(maxproduct(inpu))