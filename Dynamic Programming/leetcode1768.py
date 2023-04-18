# LeetCode 1768. Merge Strings Alternately

"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order,starting with word1.
If a string is longer than the other, append the additional letters
onto the end of the merged string.

Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ''
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1
            
        result += word1[i:] + word2[j:]

        return result 

        """
        result = ''
        i, j = 0, 0
        cnt = 0

        while(1):
            if (cnt+1) % 2 == 1: # 홀수
                if i < len(word1):
                    result += word1[i]
                    i += 1
                else:
                    result += word2[j:]
                    break
            else: # 짝수
                if j < len(word2):
                    result += word2[j]
                    j += 1
                else:
                    result += word1[i:]
                    break
            cnt += 1
        
        return result
        """
