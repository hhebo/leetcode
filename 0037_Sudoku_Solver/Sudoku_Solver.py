# -*- coding: utf-8 -*-

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    1.Each of the digits 1-9 must occur exactly once in each row.
    2.Each of the digits 1-9 must occur exactly once in each column.
    3.Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        block = [[False] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i][int(board[i][j])] = True
                    col[j][int(board[i][j])] = True
                    block[i // 3 * 3 + j // 3][int(board[i][j])] = True
        for i in range(81):
            if board[i // 9][i % 9] == '.':
                if not self._dfs(board, i, row, col, block):
                    return

    def _dfs(self, board, position, row, col, block):
        if position == 81:
            return True
        n = position + 1
        while n < 81:
            if board[n // 9][n % 9] == '.':
                break
            n += 1
        x = position // 9
        y = position % 9
        for i in range(1, 10):
            if not row[x][i] and not col[y][i] and not block[x // 3 * 3 + y // 3][i]:
                row[x][i] = True
                col[y][i] = True
                block[x // 3 * 3 + y // 3][i] = True
                board[x][y] = str(i)
                if self._dfs(board, n, row, col, block):
                    return True
                row[x][i] = False
                col[y][i] = False
                block[x // 3 * 3 + y // 3][i] = False
                board[x][y] = '.'
        return False
