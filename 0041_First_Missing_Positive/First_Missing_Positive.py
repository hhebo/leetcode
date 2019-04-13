# -*- coding: utf-8 -*-

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                hash_map[nums[i]] = True
        for i in range(1, len(nums) + 1):
            if i not in hash_map.keys():
                return i
        return len(nums) + 1
