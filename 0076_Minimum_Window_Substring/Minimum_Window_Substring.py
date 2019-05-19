# -*- coding: utf-8 -*-

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"

Output: "BANC"

Note:
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result, left, right, count, size = '', 0, 0, 0, sys.maxsize
        t_count = collections.Counter(t)
        s_count = collections.defaultdict(int)
        while right < len(s):
            s_count[s[right]] += 1
            if s[right] in t_count and s_count[s[right]] <= t_count[s[right]]:
                count += 1
            while left <= right and count == len(t):
                if size > right - left + 1:
                    size = right - left + 1
                    result = s[left:right + 1]
                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    count -= 1
                left += 1
            right += 1
        return result
