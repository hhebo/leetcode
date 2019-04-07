# -*- coding: utf-8 -*-

"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

Both dividend and divisor will be 32-bit signed integers.

The divisor will never be 0.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result
overflows.
"""


class Solution:
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return -1
        if dividend == self.MIN_INT and divisor == -1:
            return self.MAX_INT
        result = 0
        flag = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp = divisor
            count = 1
            while temp << 1 < dividend:
                temp <<= 1
                count <<= 1
            dividend -= temp
            result += count
        return result if flag else -result
