# LeetCode Problem 13 - Roman to Integer
# https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=hash-table&

# Given a roman numeral, convert it to an integer.

# Notes:

def romanToInt(s):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = None
    for i, symbol in enumerate(s):
        # If previous symbol was greater, subtract
        if prev and numerals[symbol] > numerals[prev]:
            total -= numerals[prev]
            total += numerals[symbol] - numerals[prev]
        else:
            total += numerals[symbol]
        prev = symbol
    return total
        
# Testing
print("III =>", romanToInt("III"))
print("LVIII =>", romanToInt("LVIII"))
print("MCMXCIV =>", romanToInt("MCMXCIV"))
print("IV =>", romanToInt("IV"))