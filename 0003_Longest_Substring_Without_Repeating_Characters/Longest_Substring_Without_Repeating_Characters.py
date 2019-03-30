# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 256
        left = 0
        right = -1
        result = 0
        while right + 1 < len(s):
            if freq[ord(s[right + 1])] == 0:
                right += 1
                freq[ord(s[right])] += 1
            else:
                freq[ord(s[left])] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
