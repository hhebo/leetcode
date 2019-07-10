# -*- coding: utf-8 -*-

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow = fast = head
        last = slow
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        last.next = None
        root = TreeNode(slow.val)
        if head != slow:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast)
        return root
