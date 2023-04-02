# LeetCode 942. DI String Match

"""
A permutation perm of n + 1 integers of all the integers 
in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. 
If there are multiple valid permutations perm, return any of them.

Input: s = "IDID"
Output: [0,4,1,3,2]

Input: s = "III"
Output: [0,1,2,3]

Input: s = "DDI"
Output: [3,2,0,1]
"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        min = 0
        max = len(s)
        result = []

        for i in range(len(s)):
            if s[i] == 'I':
                result.append(min)
                min += 1
            else: # D
                result.append(max)
                max -= 1
        result.append(min)
        return result
