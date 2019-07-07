# -*- coding: utf-8 -*-

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]

postorder = [9,15,7,20,3]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder and postorder):
            return None
        root, index = TreeNode(postorder[-1]), inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[1 + index:], postorder[index:-1])
        return root
