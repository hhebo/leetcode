# -*- coding: utf-8 -*-

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    1.Insert a character
    2.Delete a character
    3.Replace a character

Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

Example 2:

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) or len(word2)
        m, n = len(word1) + 1, len(word2) + 1
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            result[i][0] = i
        for j in range(m):
            result[0][j] = j
        for i in range(1, n):
            for j in range(1, m):
                if word1[j - 1] == word2[i - 1]:
                    result[i][j] = result[i - 1][j - 1]
                else:
                    result[i][j] = min(result[i - 1][j - 1], min(result[i - 1][j], result[i][j - 1])) + 1
        return result[n - 1][m - 1]
