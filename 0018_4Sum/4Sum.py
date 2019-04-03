# -*- coding: utf-8 -*-

"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        length, temp = len(nums), []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                m = j + 1
                n = length - 1
                while m < n:
                    num = nums[i] + nums[j] + nums[n] + nums[m]
                    if num < target:
                        m += 1
                    elif num > target:
                        n -= 1
                    else:
                        temp.append([nums[i], nums[j], nums[n], nums[m]])
                        m += 1
                        n -= 1
        result = []
        [result.append(t) for t in temp if t not in result]
        return result
