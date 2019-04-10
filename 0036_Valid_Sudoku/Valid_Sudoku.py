# -*- coding: utf-8 -*-

"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Only the filled cells need to be validated according to the mentioned rules.

The given board contain only digits 1-9 and the character '.'.

The given board size is always 9x9
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self._is_valid_row(board) and self._is_valid_col(board) and self._is_vaild_sq(board)

    def _is_valid_area(self, area):
        result = [e for e in area if e != '.']
        return len(set(result)) == len(result)

    def _is_valid_row(self, arr):
        for row in arr:
            if not self._is_valid_area(row):
                return False
        return True

    def _is_valid_col(self, arr):
        for col in zip(*arr):
            if not self._is_valid_area(col):
                return False
        return True

    def _is_vaild_sq(self, arr):
        for x in (0, 3, 6):
            for y in (0, 3, 6):
                sq = [arr[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]
                if not self._is_valid_area(sq):
                    return False
        return True
