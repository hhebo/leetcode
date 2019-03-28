# -*- coding: utf-8 -*-

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        length = len(nums1) + len(nums2)
        i = j = 0
        for _ in range(length):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            elif i < len(nums1):
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        half = length // 2
        return (nums[half] + nums[~half]) / 2
