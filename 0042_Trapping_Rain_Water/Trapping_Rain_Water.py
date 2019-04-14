# -*- coding: utf-8 -*-

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result, length = 0, len(height)
        left_max, right_max = [height[0]], [-1] * length
        for i in range(1, length):
            left_max.append(max(height[i], left_max[i - 1]))
        right_max[length - 1] = height[length - 1]
        for i in reversed(range(length - 1)):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, length - 1):
            result += (min(left_max[i], right_max[i]) - height[i])
        return result
