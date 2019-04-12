# -*- coding: utf-8 -*-

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self._generate(candidates, target, 0, 0, [], result)
        return result

    def _generate(self, candidates: List[int], target: int, index: int, sums: int, temp: List[int], result: List[List[int]]) -> None:
        if target == sums:
            if sorted(temp) not in result:
                result.append(copy.deepcopy(sorted(temp)))
            return
        for i in range(index, len(candidates)):
            if sums + candidates[i] <= target:
                temp.append(candidates[i])
                self._generate(candidates, target, i + 1, sums + candidates[i], temp, result)
                temp.pop()
