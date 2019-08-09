# -*- coding: utf-8 -*-

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not (board and board[0]):
            return
        n, m, queue = len(board), len(board[0]), []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i in (0, n - 1) or j in (0, m - 1)):
                    queue.append((i, j))
        while queue:
            row, col = queue.pop(0)
            if 0 <= row < n and 0 <= col < m and board[row][col] == 'O':
                board[row][col] = 'H'
                if row - 1 >= 0 and board[row - 1][col] == 'O':
                    queue.append((row - 1, col))
                if row + 1 < n and board[row + 1][col] == 'O':
                    queue.append((row + 1, col))
                if col - 1 >= 0 and board[row][col - 1] == 'O':
                    queue.append((row, col - 1))
                if col + 1 < m and board[row][col + 1] == 'O':
                    queue.append((row, col + 1))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'H':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
