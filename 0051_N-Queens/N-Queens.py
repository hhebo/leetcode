# -*- coding: utf-8 -*-

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4

Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result, current = [], [['.'] * n for _ in range(n)]
        self._solve(current, n, 0, result)
        return result

    def _solve(self, cur, n, row, res):
        if row == len(cur):
            t = [''.join(e) for e in cur]
            res.append(t)
            return
        for col in range(len(cur)):
            if self._isValid(cur, row, col):
                cur[row][col] = 'Q'
                self._solve(cur, n, row + 1, res)
                cur[row][col] = '.'

    def _isValid(self, cur, row, col):
        for i in range(row):
            if cur[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if cur[i][j] == 'Q':
                return False
            i, j = i - 1, j - 1
        i, j = row - 1, col + 1
        while i >= 0 and j < len(cur):
            if cur[i][j] == 'Q':
                return False
            i, j = i - 1, j + 1
        return True
