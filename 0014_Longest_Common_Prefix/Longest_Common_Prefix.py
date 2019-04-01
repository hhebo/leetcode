# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]
        length = len(result)
        for i in range(1, len(strs)):
            while not strs[i].startswith(result):
                result = result[0:length - 1]
                length -= 1
        return result
