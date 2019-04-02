# -*- coding: utf-8 -*-

"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        flag = sys.maxsize
        result = 0
        for i in range(length - 2):
            left = i + 1
            right = length - 1
            while left < right:
                if target > (nums[i] + nums[left] + nums[right]):
                    if target - (nums[i] + nums[left] + nums[right]) < flag:
                        flag = target - (nums[i] + nums[left] + nums[right])
                        result = nums[i] + nums[left] + nums[right]
                    left += 1
                elif target < (nums[i] + nums[left] + nums[right]):
                    if (nums[i] + nums[left] + nums[right]) - target < flag:
                        flag = (nums[i] + nums[left] + nums[right]) - target
                        result = nums[i] + nums[left] + nums[right]
                    right -= 1
                else:
                    return target
        return result
