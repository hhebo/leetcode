# -*- coding: utf-8 -*-

"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]

Output: [0,9]

Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]

Output: []
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not (s and words):
            return []
        result, hash_map = [], {}
        for i in range(len(words)):
            if words[i] in hash_map.keys():
                hash_map[words[i]] += 1
            else:
                hash_map[words[i]] = 1
        for i in range(len(s) - len(words[0]) * len(words) + 1):
            j, temp = 0, {}
            while j < len(words):
                w = s[i + j * len(words[0]): i + (j + 1) * len(words[0])]
                if w not in hash_map.keys():
                    break
                if w in temp.keys():
                    temp[w] += 1
                else:
                    temp[w] = 1
                if temp[w] > hash_map[w]:
                    break
                j += 1
            if j >= len(words):
                result.append(i)
        return result
