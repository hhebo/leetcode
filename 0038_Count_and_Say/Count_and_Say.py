# -*- coding: utf-8 -*-

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        if n == 1:
            return s
        for _ in range(1, n):
            s = self._next(s)
        return s

    def _next(self, s):
        result, start = '', 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] != s[start]:
                result += str(i - start) + s[start]
                start = i
        return result
