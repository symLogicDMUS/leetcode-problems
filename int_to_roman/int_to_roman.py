import sys

from int_to_roman.split_n import split_n
from int_to_roman.order_of_magnitude import order_of_magnitude
from int_to_roman.order_of_magnitude_adjust import order_of_magnitude_adjust

def int_to_roman(num):
    """ """
    l = split_n(num)
    m = order_of_magnitude(l)
    m = order_of_magnitude_adjust(m)
    roman = ""
    for c in m:
        roman += c
    return roman

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/integer-to-roman/ """
    for arg in sys.argv[1:]:
        print("{}".format(arg), int_to_roman(int(arg)))