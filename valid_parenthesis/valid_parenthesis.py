import sys

from valid_parenthesis.is_unbalanced import is_unbalanced


def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    closes = {']': '[', '}': '{', ')': '('}

    if is_unbalanced(s):
        return False

    stack = []

    for c in s:
        if c in closes.keys():
            if len(stack) == 0:
                return False
            r = stack.pop()
            if closes[c] != r:
                return False
        else:
            stack.append(c)
    return True

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/valid-parentheses """
    for arg in sys.argv[1:]:
        is_valid(arg)