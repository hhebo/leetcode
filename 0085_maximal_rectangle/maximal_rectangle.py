# -*- coding: utf-8 -*-

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

Output: 6
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        result = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heights[j] = 0 if matrix[i][j] == '0' else 1 + heights[j]
            result = max(result, self._largest_rectangle_area(heights))
        return result

    def _largest_rectangle_area(self, heights: List[int]) -> int:
        heights.append(0)
        stack, result, i = [], 0, 0
        while i < len(heights):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                current = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                result = max(result, heights[current] * width)
        return result
