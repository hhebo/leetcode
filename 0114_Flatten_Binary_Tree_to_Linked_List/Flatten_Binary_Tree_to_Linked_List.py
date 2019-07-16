# -*- coding: utf-8 -*-

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        temp, root.right, root.left = root.right, root.left, None
        while root.right:
            root = root.right
        root.right = temp
