# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]

Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result, nums_set = 0, set(nums)
        for num in nums:
            pre_value, next_value = num - 1, num + 1
            while pre_value in nums_set:
                nums_set.remove(pre_value)
                pre_value -= 1
            while next_value in nums_set:
                nums_set.remove(next_value)
                next_value += 1
            result = max(result, next_value - pre_value - 1)
        return result
