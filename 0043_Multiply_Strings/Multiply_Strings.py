# -*- coding: utf-8 -*-

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
    1. The length of both num1 and num2 is < 110.
    2. Both num1 and num2 contain only digits 0-9.
    3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)
        result, index = '', 0
        for i in reversed(range(len1)):
            for j in reversed(range(len2)):
                temp = int(num1[i]) * int(num2[j]) + res[i + j + 1]
                res[i + j + 1] += temp % 10
                res[i + j] += temp // 10
        while index < len(res):
            if res[index] != 0:
                break
            index += 1
        for i in range(index, len(res)):
            result += str(res[i])
        return result
