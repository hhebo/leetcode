# -*- coding: utf-8 -*-

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        result = []
        for k, v in enumerate(nums):
            try:
                d[v].append(k)
            except KeyError:
                d[v] = [k]
        nums = sorted(set(nums))
        length = len(nums)
        for i in range(length - 2):
            left = i + 1
            right = length - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        for k in d:
            if k == 0 and len(d.get(k)) > 2:
                result.append([0, 0, 0])
                continue
            if len(d.get(k)) > 1 and k != 0 and d.get(-2 * k) is not None:
                result.append(sorted([k, k, -2 * k]))
        return result
