# -*- coding: utf-8 -*-

"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        (x, n) = (1 / x, -n) if n < 0 else (x, n)
        return self._power(x, n)

    def _power(self, x, n):
        if n == 0:
            return 1.
        return self._power(x * x, n // 2) * (x if n % 2 else 1)
