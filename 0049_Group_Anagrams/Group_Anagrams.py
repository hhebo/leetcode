# -*- coding: utf-8 -*-

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result, hash_map = [], {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hash_map.keys():
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        for _, v in hash_map.items():
            result.append(v)
        return result
