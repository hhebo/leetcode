# -*- coding: utf-8 -*-

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]

Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, size, last = [[]], 1, nums[0]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != last:
                last, size = nums[i], len(result)
            new_size = len(result)
            for j in range(new_size - size, new_size):
                result.append(copy.deepcopy(result[j]))
                result[-1].append(nums[i])
        return result
