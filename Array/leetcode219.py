# LeetCode 219. Contains Duplicate II

"""
Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(list(set(nums))) == len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(1, k+1):
                if i+j > len(nums)-1
                    continue
                if nums[i] == nums[i+j]:
                    return True
        return False
