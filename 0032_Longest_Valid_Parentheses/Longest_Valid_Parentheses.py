# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result, stack = 0, [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    # 记录（ 的前一个下标
                    stack.append(i)
                else:
                    result = result if result > i - stack[-1] else i - stack[-1]
        return result
