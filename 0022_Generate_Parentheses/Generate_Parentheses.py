# -*- coding: utf-8 -*-

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._generate(result, '', 0, 0, n)
        return result

    def _generate(self, result: List[str], s: str, left: int, right: int, n: int) -> None:
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            self._generate(result, s + '(', left + 1, right, n)
        if right < left:
            self._generate(result, s + ')', left, right + 1, n)
