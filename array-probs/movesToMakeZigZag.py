# LeetCode Problem 1144 - Decrease Elements To Make Array ZigZag
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag

# Given an array nums of integers, a move consists of choosing any 
# element and decreasing it by 1. Return the minimum number of moves
# to transform the given array nums into a zigzag array.

# Notes:
    # Can only decrease elements
    # Either even peaks or odd peaks
    # One move = decrease an element by 1
    # Time Complexity: O(n)
        # Only loop through arraytwice
    # Space Complexity:O(1)
    # Greedy !!!

class Solution(object):
    def movesToMakeZigzag(self,nums):
        n = len(nums)

        # Calculates num of moves for pattern
        def moves(pattern): # pattern = 0 for EVEN peaks, 1 for ODD
            total = 0
            for i in range(n):
                # If i is not at the beginning of the list
                    # Assign left with left neighbor
                # Else, left = "infinity" (no neighbor)
                left = nums[i - 1] if i - 1 >= 0 else float('inf')
                # If i is not at end of the list (...)
                right = nums[i + 1] if i + 1 < n else float('inf')
                if i % 2 == pattern:
                    continue # skip peaks
                # i == VALLEY
                min_neighbor = min(left, right)
                # Fix zigzag violation
                if nums[i] >= min_neighbor:
                    total += nums[i] - min_neighbor + 1
            return total
        # Try both patterns, return lowest num of moves
        return min(moves(0), moves(1))

# ----------------------------
# MAIN FUNCT WITH TEST CASES
# ----------------------------

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [1, 2, 3],          # Output: 2
        [9, 6, 1, 6, 2],    # Output: 4
        [2, 7, 10, 9, 8],   # Output: 4
        [10, 5, 10],        # Output: 0
        [1]                 # Output: 0
    ]

    for i, nums in enumerate(test_cases):
        result = solution.movesToMakeZigzag(nums)
        print(f"Test case {i + 1}: Input = {nums} -> Output = {result}")