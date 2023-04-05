# LeetCode 409. Longest Palindrome

"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        result = 0
        odd = 0

        for k in count:
            result += (count[k] // 2) * 2
            if count[k] % 2 > 0:
                odd = 1
        return result + odd
