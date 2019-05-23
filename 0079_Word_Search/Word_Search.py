# -*- coding: utf-8 -*-

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not (board and board[0]):
            return False
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._search(board, word, 0, i, j, visited):
                    return True
        return False

    def _search(self, board: List[List[str]], word: str, idx: int, i: int, j: int, visited: List[List[bool]]) -> bool:
        if idx == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j] or word[idx] != board[i][j]:
            return False
        visited[i][j] = True
        res = \
            self._search(board, word, idx + 1, i - 1, j, visited) or \
            self._search(board, word, idx + 1, i + 1, j, visited) or \
            self._search(board, word, idx + 1, i, j - 1, visited) or \
            self._search(board, word, idx + 1, i, j + 1, visited)
        visited[i][j] = False
        return res
