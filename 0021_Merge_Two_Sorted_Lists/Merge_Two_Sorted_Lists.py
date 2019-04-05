# -*- coding: utf-8 -*-

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4

Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        current = result
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
        current.next = l1 or l2 or None
        return result.next
