# -*- coding: utf-8 -*-

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        self._find(result, [], root, sum)
        return result

    def _find(self, result: List[List[int]], temp: List[int], root: TreeNode, sum: int) -> None:
        if root is None:
            return
        temp.append(root.val)
        if root.val == sum and root.left is None and root.right is None:
            result.append(temp[:])
        self._find(result, temp, root.left, sum - root.val)
        self._find(result, temp, root.right, sum - root.val)
        temp.pop()
