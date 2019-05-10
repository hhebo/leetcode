# -*- coding: utf-8 -*-

"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:
    Input:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    Output:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]

Example 2:
    Input:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    Output:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
    Input:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
             "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    Output:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, i = [], 0
        while i < len(words):
            j, length = i, 0
            while j < len(words) and length + len(words[j]) + j - i <= maxWidth:
                length, j = length + len(words[j]), j + 1
            out, space = '', maxWidth - length
            for k in range(i, j):
                out += words[k]
                if space > 0:
                    if j == len(words):
                        if j - k == 1:
                            temp = space
                        else:
                            temp = 1
                    else:
                        if j - k - 1 > 0:
                            if space % (j - k - 1) == 0:
                                temp = space // (j - k - 1)
                            else:
                                temp = space // (j - k - 1) + 1
                        else:
                            temp = space
                    out, space = out + ' ' * temp, space - temp
            result.append(out)
            i = j
        return result
