# -*- coding: utf-8 -*-

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4

Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        pre = dummy
        dummy.next = head
        for _ in range(m - 1):
            pre = pre.next
        current = pre.next
        for _ in range(m, n):
            temp = current.next
            current.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next
