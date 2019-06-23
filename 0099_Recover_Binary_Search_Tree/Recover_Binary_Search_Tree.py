# -*- coding: utf-8 -*-

"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result, vals = [], []
        self._inorder(root, result, vals)
        vals.sort()
        for i in range(len(result)):
            result[i].val = vals[i]

    def _inorder(self, root: TreeNode, res: List[TreeNode], vals: List[int]) -> None:
        if root:
            self._inorder(root.left, res, vals)
            res.append(root)
            vals.append(root.val)
            self._inorder(root.right, res, vals)
