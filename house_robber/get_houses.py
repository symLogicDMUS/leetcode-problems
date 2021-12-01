from pprint import pprint

from is_odd import is_odd


def get_odd_houses(nums):
    odd_houses = []
    for i in range(len(nums)):
        if not is_odd(i):
            odd_houses.append(nums[i])
    return odd_houses

def get_even_houses(nums):
    odd_houses = []
    for i in range(len(nums)):
        if is_odd(i):
            odd_houses.append(nums[i])
    return odd_houses

if __name__ == '__main__':
    pprint(get_odd_houses([3, 2, 6, 1, 5, 3, 4, 0, 2]))
    pprint(get_even_houses([3, 2, 6, 1, 5, 3, 4, 0, 2]))