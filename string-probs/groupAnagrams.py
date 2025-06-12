# LeetCode Problem 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams

# Given an array of strings strs, group the anagrams 
# together. You can return the answer in any order.

# Notes:
    # An anagram is a word or phrase formed by rearranging
        # the letters of a different word or phrase, using 
        # all the original letters exactly once.
    # Time Complexity Analysis:
        # Sorting each string: O(k logk)
        # Iterating through all strings: O(n)
        # Hash map insertion: negligible
        # Overall: O(n * k logk)
        
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
            # key: sorted string
            # value: list of all anagrams

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)

        return list(anagrams.values())


# ----------------------------
# MAIN FUNCT WITH TEST CASES
# ----------------------------

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
    ]

    for i, strs in enumerate(test_cases, 1):
        result = solution.groupAnagrams(strs)
        print(f"Test Case {i}:")
        print(f"Input: {strs}")
        print(f"Grouped Anagrams: {result}\n")