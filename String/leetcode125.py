# LeetCode 125. Valid Palindrome

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

예제1
Input: s = "A man, a plan, a canal: Panama"
Output: true

예제2
Input: s = "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                alpha += s[i].lower()

        rev_list = list(reversed(list(alpha)))

        return ''.join(rev_list) == alpha
