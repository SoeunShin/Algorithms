# 94. Binary Tree Inorder Traversal

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if node is not None: # inorder(중위순회)
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)
        
        dfs(root) # 함수 호출
        return ans
