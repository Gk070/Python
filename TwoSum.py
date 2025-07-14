# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            elif nums[i] + nums[j] == target:
                return i,j

i, j = twoSum(nums, target)
print(i, j)