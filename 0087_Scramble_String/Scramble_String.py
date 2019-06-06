# -*- coding: utf-8 -*-

"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"

Output: true

Example 2:

Input: s1 = "abcde", s2 = "caebd"

Output: false
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        length = len(s1)
        dp = [[[0] * length for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if s1[i] == s2[j]:
                    dp[0][i][j] = 1
        for k in range(length):
            for i in range(length - k):
                for j in range(length - k):
                    if dp[k][i][j] == 0:
                        for n in range(k):
                            if (dp[n][i][j] and dp[k - n - 1][i + n + 1][j + n + 1]) or (
                                    dp[n][i][j + k - n] and dp[k - n - 1][i + n + 1][j]):
                                dp[k][i][j] = 1
        return dp[-1][0][0] == 1
