import sys


def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    s = s.replace("IV", "IIII")
    s = s.replace("IX", "IIIIIIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "XXXXXXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "CCCCCCCCC")

    value = 0
    for c in s:
        value += roman_values[c]
    return value

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/roman-to-integer/ """
    for arg in sys.argv[1:]:
        roman_to_int(arg)