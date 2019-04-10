# -*- coding: utf-8 -*-

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                i = j = mid
                while i > 0 and nums[i] == nums[i - 1]:
                    i -= 1
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                return [i, j]
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]
