# -*- coding: utf-8 -*-

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = index = 0
        while (index < len(s)):
            start = end = index
            index += 1
            while index < len(s) and s[index] == s[start]:
                index += 1
            end = index - 1
            while start - 1 >= 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
            if right - left < end - start:
                right = end
                left = start
        return s[left:(right + 1)]
