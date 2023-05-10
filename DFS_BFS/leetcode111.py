# LeetCode 111. Minimum Depth of Binary Tree

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSubtreeSymmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isSubtreeSymmetric(left.left, right.right) and isSubtreeSymmetric(right.right, left.left)
        return isSubtreeSymmetric(root, root)
