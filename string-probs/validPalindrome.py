# LeetCode Problem 125 - Valid Palindrome
# https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric on the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric on the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# ----------------------------
# MAIN FUNCT WITH TEST CASES
# ----------------------------

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("hello", False),
        ("Hannah", True),
        ("", True),
        ("12321", True),
        ("rAce!!!car", True),
        ("Nope", False)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.isPalindrome(s)
        print(f"Test case {i}: {'PASSED' if result == expected else 'FAILED'}\n")