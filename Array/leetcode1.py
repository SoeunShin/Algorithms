# LeetCode 1. Two Sum

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

예제1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

예제2
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            tmp = target - n

            if tmp in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(tmp) + (i+1)]
