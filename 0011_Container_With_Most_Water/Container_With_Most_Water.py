# -*- coding: utf-8 -*-

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, left, right = 0, 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                temp = height[left] * (right - left)
                left += 1
            else:
                temp = height[right] * (right - left)
                right -= 1
            result = max(result, temp)
        return result
