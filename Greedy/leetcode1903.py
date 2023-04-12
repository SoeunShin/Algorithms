# 1903. Largest Odd Number in String

"""
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) 
that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Input: num = "52"
Output: "5"

Input: num = "4206"
Output: ""

Input: num = "35427"
Output: "35427"
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)):
            if int(num[-1]) % 2 == 0:
                num = num[:-1]
        return num
