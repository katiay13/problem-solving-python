# LeetCode Problem 3 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Given a string s, find the length of the longest substring without duplicate 
# characters.

# Notes:
    # sliding window problem !!
    # 'right' pointer moves forward one character at a time to expand window
    # 'left' pointer moves forward only if there is a REPEAT to shrink window
    # 'seen' holds unique characters in the current window

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # seen = keeps track of characters in substring
        seen = set()
        left = 0 # left pointer, beginning of substring
        max_len = 0 # maximum length of valid substrings

        # iterate over each character in the string w 'right'
        # 'right' = end of sliding window
        for right in range(len(s)):
            # check if current char is in 'seen' = REPEAT
            while s[right] in seen:
                # shrink window by 1 and update 'seen'
                seen.remove(s[left])
                left += 1
            seen.add(s[right])

            # update max_len with len of current valid window
            max_len = max(max_len, right - left + 1)

        return max_len

# ----------------------------
# MAIN FUNCT WITH TEST CASES
# ----------------------------

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("", 0),
        ("abcabcbb", 3),
        ("aaa", 1),
        ("ab", 2),
        ("workworking", 7)
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution.lengthOfLongestSubstring(input_str)
        print(f"Test case {i}: Input = '{input_str}' | Expected = {expected} | Got = {result}")
        print(f"{'PASS' if result == expected else 'FAIL'}\n")