# LeetCode 1323. Maximum 69 Number

"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        result = []
        flag = 0
        for i in str(num):
            if i == '6' and flag == 0:
                result.append('9')
                flag = 1
            else:
                result.append(i)
        return int(''.join(result))
