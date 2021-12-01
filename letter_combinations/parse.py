from typing import List

from letter_combinations.char_map import char_map


def parse(L, P) -> [List[str], List[List[str]]]:
    P = char_map(P, L[0])
    if len(L) == 1:
        return L, P
    else:
        L.pop(0)
        L, P = parse(L, P)
    return L, P