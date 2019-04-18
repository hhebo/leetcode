# -*- coding: utf-8 -*-

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]

Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self._generate(result, 0, nums)
        return result

    def _generate(self, res: List[List[int]], index: int, nums: List[int]) -> None:
        if index == len(nums) and nums not in res:
            res.append(copy.deepcopy(nums))
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self._generate(res, index + 1, nums)
            nums[i], nums[index] = nums[index], nums[i]
