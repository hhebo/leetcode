# -*- coding: utf-8 -*-

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]

Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        length = len(lists)
        while length > 1:
            mid = (length + 1) // 2
            for i in range(length // 2):
                lists[i] = self._merge(lists[i], lists[i + mid])
            length = mid
        return lists[0]

    def _merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        res = ListNode(-1)
        cur = res
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
        cur.next = l1 or l2 or None
        return res.next
