# -*- coding: utf-8 -*-

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"

Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self._helper(s, [], result)
        return result

    def _helper(self, s: str, path: List[str], res: List[str]) -> None:
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            cur = s[:i + 1]
            if (cur[0] == '0' and len(cur) >= 2) or int(cur) > 255:
                continue
            self._helper(s[i + 1:], path + [s[:i + 1]], res)
