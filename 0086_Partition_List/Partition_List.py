# -*- coding: utf-8 -*-

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3

Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre, cur = dummy, head
        while pre.next and pre.next.val < x:
            pre = pre.next
        cur = pre
        while cur.next:
            if cur.next.val < x:
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
                pre = pre.next
            else:
                cur = cur.next
        return dummy.next
