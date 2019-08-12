# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"

Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self._helper(s, 0, [], result)
        return result

    def _helper(self, s: str, index: int, temp: List[str], result: List[List[str]]) -> None:
        if index == len(s):
            result.append(copy.deepcopy(temp))
        for i in range(index, len(s)):
            if s[index:i] != s[i:index:-1]:
                continue
            temp.append(s[index:i + 1])
            self._helper(s, i + 1, temp, result)
            temp.pop()
