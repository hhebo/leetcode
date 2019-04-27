# -*- coding: utf-8 -*-

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result, nums, f, k = '', '123456789', [1], k-1
        for i in range(1, n):
            f.append(f[i-1] * i)
        for i in range(n, 0, -1):
            j = k // f[i - 1]
            k %= f[i - 1]
            result += nums[j]
            nums = nums.replace(nums[j], '')
        return result
