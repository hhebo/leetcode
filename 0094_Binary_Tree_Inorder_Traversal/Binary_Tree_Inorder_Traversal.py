# -*- coding: utf-8 -*-

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]

   1
    \
     2
    /
   3

Output: [1,3,2]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self._inorder(result, root)
        return result

    def _inorder(self, result: List[int], root: TreeNode) -> None:
        if root:
            self._inorder(result, root.left)
            result.append(root.val)
            self._inorder(result, root.right)
