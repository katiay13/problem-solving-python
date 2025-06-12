# LeetCode Problem 35 - Search Insert Position
# https://leetcode.com/problems/search-insert-position
#
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.
#
# Must run in O(log n) time, so binary search is used.

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid # Target found
        elif nums[mid] < target:
            left = mid + 1 # Search right
        else:
            right = mid - 1 # Search left

    # If target not found, return insert position
    return left

# Test cases!
if __name__ == "__main__":
    arr = sorted([5,2,7,3,9,1,8])
    print(searchInsert(arr, 3)) # Output: 2
    print(searchInsert(arr, 5)) # Output: 3
    print(searchInsert(arr, 8)) # Output: 5
    print(searchInsert(arr, 1)) # Output: 0
    print(searchInsert(arr, 7)) # Output: 4