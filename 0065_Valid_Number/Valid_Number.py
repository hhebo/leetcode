# -*- coding: utf-8 -*-

"""
Validate if a given string can be interpreted as a decimal number.

Some examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
    Numbers 0-9
    Exponent - "e"
    Positive/negative sign - "+"/"-"
    Decimal point - "."

Of course, the context of these characters also matters in the input.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        length = len(s)
        dot = e = digit = False
        if s[0] == '.':
            dot = True
        elif s[0].isdigit():
            digit = True
        elif s[0] not in ['-', '+']:
            return False
        for i in range(1, length - 1):
            if s[i].isdigit():
                digit = True
            elif s[i] == 'e':
                if not e and digit and s[i - 1] not in ['-', '+']:
                    e = True
                else:
                    return False
            elif s[i] in ['-', '+']:
                if s[i - 1] != 'e':
                    return False
            elif s[i] == '.':
                if not (dot or e):
                    dot = True
                else:
                    return False
            else:
                return False
        if s[length - 1].isdigit():
            return True
        return s[length - 1] == '.' and not (dot or e) and digit
