# LeetCode 561. Array Partition

"""
Given an integer array nums of 2n integers,
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized.
Return the maximized sum.

예제1
Input: nums = [1,4,3,2]
Output: 4

예제2
Input: nums = [6,2,6,5,1,2]
Output: 9
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        tot = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                tot += min(pair)
                pair = []
        return tot

        """
        return sum(sorted(nums)[::2])
        """
