# -*- coding: utf-8 -*-

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"

Output: true

Example 2:

Input: "race a car"

Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if c.isalnum()]
        return s == s[::-1]
