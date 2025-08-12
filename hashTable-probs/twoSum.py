# LeetCode Problem 1 - Two Sum
# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=hash-table

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

# Notes:
    # Use python dict (ordered)

def twoSum(nums, target):
    complements = {}    # Maps num to index in nums[]
    for i, num in enumerate(nums):
        comp = target - num
        if comp in complements:
            return [complements[comp], i]
        else:
            complements[num] = i


# Testing
print(twoSum([3,2,4], 6))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 3], 6))