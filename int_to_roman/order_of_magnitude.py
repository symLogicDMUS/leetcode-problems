from typing import List
from int_to_roman.order_of import order_1, order_10, order_100, order_1000


def order_of_magnitude(l: List[int]):
    if len(l) == 1:
        return [order_1(l[0])]
    if len(l) == 2:
        return [order_10(l[0]), order_1(l[1])]
    if len(l) == 3:
        return [order_100(l[0]), order_10(l[1]), order_1(l[2])]
    if len(l) == 4:
        return [order_1000(l[0]), order_100(l[1]), order_10(l[2]), order_1(l[3])]