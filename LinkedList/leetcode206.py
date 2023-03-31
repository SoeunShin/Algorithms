# LeetCode 206. Reverse Linked List

"""
Given the head of a singly linked list, reverse the list,
and return the reversed list.

예제1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

예제2
Input: head = [1,2]
Output: [2,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        return prev

    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
    """
