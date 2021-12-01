from typing import List

from order_of import order_1_adjust, order_10_adjust, order_100_adjust


def order_of_magnitude_adjust(romans: List[str]):
    if len(romans) == 1:
        return [order_1_adjust(romans[0])]
    if len(romans) == 2:
        return [order_10_adjust(romans[0]), order_1_adjust(romans[1])]
    if len(romans) == 3:
        return [order_100_adjust(romans[0]), order_10_adjust(romans[1]), order_1_adjust(romans[2])]
    if len(romans) == 4:
        return [romans[0], order_100_adjust(romans[1]), order_10_adjust(romans[2]), order_1_adjust(romans[3])]