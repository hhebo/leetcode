# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"

Output: 1

Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution:
    def minCut(self, s: str) -> int:
        if s is None:
            return 0
        dp, p = [0] * len(s), [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i] = i
            for j in range(i + 1):
                if s[i] == s[j] and (((i - j) < 2) or p[j + 1][i - 1]):
                    p[j][i] = True
                    dp[i] = 0 if j == 0 else min(dp[i], dp[j - 1] + 1)
        return dp[len(s) - 1]
