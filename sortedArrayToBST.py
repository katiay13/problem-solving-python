# LeetCode Problem 108 - Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# Height balanced -> Height diff between left & right subtrees is no more than 1

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:      # List is empty
            return None   # None = null

        mid = len(nums) // 2    # Middle index
        root = TreeNode(nums[mid])  # Create TreeNode with mid value
        # nums[:mid] =  sublist from index 0 to (mid - 1)
        root.left = self.sortedArrayToBST(nums[:mid])
        # nums[mid+1:] = sublist from index mid+1 to end
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

# Prints level-order traversal (breadth-first)
def print_level_order(root):
    if not root:
        print("Tree is empty.")
        return

    queue = deque([root])
    result = [] # Stores values in level order

    while queue: # Loop until queue is empty
        node = queue.popleft()
        if node: # If node exists
            result.append(node.val) # Add val to result list
            # Add both children to queue, even if null/None
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    # Remove edge "null" values
    # While result != empty && last item == null
    while result and result[-1] == "null":
        result.pop()

    print("Level-order:", result)

# Main function w test cases
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [-10, -3, 0, 5, 9],
        [1, 3],
        [0],
        [],
        [-5, -3, -1, 0, 2, 4, 6]
    ]

    for i, nums in enumerate(test_cases):
        print(f"\nTest case{i + 1}: Input = {nums}")
        tree_root = solution.sortedArrayToBST(nums)
        print_level_order(tree_root)