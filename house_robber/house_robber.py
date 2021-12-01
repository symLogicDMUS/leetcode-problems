from pprint import pprint

from get_houses import get_odd_houses, get_even_houses
from is_odd import is_odd

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int

    even length array means there is same # even as odd numbers.
    ood length array means 1 more odd than even

    """
    odd_houses = get_odd_houses(nums)
    even_houses = get_even_houses(nums)

    odd_sum = sum(odd_houses)
    even_sum = sum(even_houses)

    return max(odd_sum, even_sum)

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/house-robber/ (not solved)"""
    pprint(rob([3, 2, 6, 1, 5, 3, 4, 0, 2]))
