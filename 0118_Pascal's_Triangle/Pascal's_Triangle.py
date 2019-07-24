# -*- coding: utf-8 -*-

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5

Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(temp)
        return res
