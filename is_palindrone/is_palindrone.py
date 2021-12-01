import sys


def is_palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    str_x = str(x)
    arr_x = list(str_x)
    arr_x.reverse()
    x_reverse = "".join(arr_x)
    if str_x == x_reverse:
        return True
    else:
        return False

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/palindrome-number/"""
    for x in sys.argv[1:]:
        is_palindrome(int(x))