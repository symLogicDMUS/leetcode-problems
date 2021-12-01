import sys
from pprint import pprint

from multiply_strings.split_n import split_n
from multiply_strings.get_zeros import get_zeros
from multiply_strings.add_zeros import add_zeros
from multiply_strings.resolve_mags import resolve_mags
from multiply_strings.sum_int_mags import sum_int_mags


def resolve_number(num):
    """take number as string and return in integer form without using built-in methods"""
    digits = split_n(num)
    zeros = get_zeros(len(digits))
    mags = add_zeros(digits, zeros)
    int_mags = resolve_mags(mags)
    int_num = sum_int_mags(int_mags)
    return int_num

if __name__ == '__main__':
    pprint(resolve_number(sys.argv[1]))