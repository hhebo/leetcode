# -*- coding: utf-8 -*-

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        result = ''
        if x < 0:
            result += '-'
            x = -x
        while x // 10 and x % 10 == 0:
            x //= 10
        while x // 10:
            result += str(x % 10)
            x //= 10
        result += str(x)
        result = int(result)
        if result < self.INT_MIN or result > self.INT_MAX:
            return 0
        return result
