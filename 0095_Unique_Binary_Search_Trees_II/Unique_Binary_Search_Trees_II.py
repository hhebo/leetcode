# -*- coding: utf-8 -*-

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3

Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

Explanation:

The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self._generate(1, n)

    def _generate(self, start: int, end: int) -> List[TreeNode]:
        result = []
        if start > end:
            result.append(None)
        for i in range(start, end + 1):
            lefts = self._generate(start, i - 1)
            rights = self._generate(i + 1, end)
            for left in lefts:
                for right in rights:
                    root = TreeNode(i)
                    root.left, root.right = left, right
                    result.append(root)
        return result
