# -*- coding: utf-8 -*-

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2

Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self._generate(n, k, 1, [], result)
        return result

    def _generate(self, n: int, k: int, start: int, temp: List[int], result: List[List[int]]) -> None:
        if len(temp) == k:
            result.append(copy.deepcopy(temp))
            return
        for i in range(start, n + 1):
            temp.append(i)
            self._generate(n, k, i + 1, temp, result)
            temp.pop()
