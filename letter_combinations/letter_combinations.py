import sys
from pprint import pprint
from typing import List

from letter_combinations.map_digits import map_digits
from letter_combinations.parse import parse


def letter_combinations(digits: str) -> List[str]:
    if digits == "":
        return []
    L = map_digits(digits)
    if len(L) == 1:
        return L[0]
    P = L.pop(0)
    L, P = parse(L, P)
    P.sort()
    return P


if __name__ == '__main__':
    """problem URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/"""
    pprint(letter_combinations(sys.argv[1]))