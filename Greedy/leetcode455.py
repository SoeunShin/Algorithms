# LeetCode 455. Assign Cookies

"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Input: g = [1,2,3], s = [1,1]
Output: 1

Input: g = [1,2], s = [1,2,3]
Output: 2
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = cookie = 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
