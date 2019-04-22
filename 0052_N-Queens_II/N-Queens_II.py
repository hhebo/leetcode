# -*- coding: utf-8 -*-

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4

Output: 2

Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:
    def __init__(self) -> None:
        self.result = 0

    def totalNQueens(self, n: int) -> int:
        cur = [['.'] * n for _ in range(n)]
        self._solve(cur, n, 0)
        return self.result

    def _solve(self, cur: List[List[str]], n: int, row: int) -> None:
        if row == len(cur):
            self.result += 1
            return
        for col in range(len(cur)):
            if self._isValid(cur, row, col):
                cur[row][col] = 'Q'
                self._solve(cur, n, row + 1)
                cur[row][col] = '.'

    def _isValid(self, cur: List[List[str]], row: int, col: int) -> bool:
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
