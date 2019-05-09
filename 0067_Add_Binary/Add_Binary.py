# -*- coding: utf-8 -*-

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"

Output: "100"

Example 2:

Input: a = "1010", b = "1011"

Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, m, n, temp = '', len(a) - 1, len(b) - 1, 0
        while m >= 0 or n >= 0:
            s1 = int(a[m]) if m >= 0 and a[m] > '0' else 0
            s2 = int(b[n]) if n >= 0 and b[n] > '0' else 0
            result = str((s1 + s2 + temp) % 2) + result
            temp, m, n = (s1 + s2 + temp) // 2, m - 1, n - 1
        return result if temp == 0 else '1' + result
