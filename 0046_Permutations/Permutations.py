# -*- coding: utf-8 -*-

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]

Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self._generate(result, 0, nums)
        return result

    def _generate(self, result: List[List[int]], index: int, nums: List[int]):
        if index == len(nums):
            result.append(copy.deepcopy(nums))
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self._generate(result, index + 1, nums)
            nums[i], nums[index] = nums[index], nums[i]
