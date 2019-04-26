# -*- coding: utf-8 -*-

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3

Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result, val = [[0] * n for _ in range(n)], 1
        left, up, right, down = 0, 0, n - 1, n - 1
        while True:
            for j in range(left, right + 1):
                result[left][j], val = val, val + 1
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                result[i][right], val = val, val + 1
            right -= 1
            if left > right:
                break
            for j in range(right, left - 1, -1):
                result[down][j], val = val, val + 1
            down -= 1
            if up > down:
                break
            for i in range(down, up - 1, -1):
                result[i][left], val = val, val + 1
            left += 1
            if left > right:
                break
        return result
