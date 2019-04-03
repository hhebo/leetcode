# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                result.append(s[i])
                continue
            if s[i] == ')' and (len(result) == 0 or result.pop() != '('):
                return False
            if s[i] == ']' and (len(result) == 0 or result.pop() != '['):
                return False
            if s[i] == '}' and (len(result) == 0 or result.pop() != '{'):
                return False
        return True if len(result) == 0 else False

