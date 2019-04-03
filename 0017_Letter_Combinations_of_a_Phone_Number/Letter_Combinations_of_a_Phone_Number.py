# -*- coding: utf-8 -*-

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    LETTERS = [[l for l in s] for s in ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxzy']]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits is '':
            return []
        digits = [int(digit) for digit in digits]
        result = []
        self._generate(result, '', 0, digits)
        return result

    def _generate(self, result: List[str], temp: str, index: int, digits: List[int]) -> None:
        if index == len(digits):
            result.append(temp)
            return
        for i in range(len(self.LETTERS[digits[index]])):
            self._generate(result, temp + self.LETTERS[digits[index]][i], index + 1, digits)
