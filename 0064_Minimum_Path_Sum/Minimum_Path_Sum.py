# -*- coding: utf-8 -*-

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7

Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        result = [[0]*n for _ in range(m)]
        result[0][0] = grid[0][0]
        for i in range(1, m):
            result[i][0] = grid[i][0] + result[i - 1][0]
        for j in range(1, n):
            result[0][j] = grid[0][j] + result[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = grid[i][j] + min(result[i][j - 1], result[i - 1][j])
        return result[m - 1][n - 1]
