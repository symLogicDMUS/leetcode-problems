from pprint import pprint


def get_zeros(n):
    """n is length of number, e.g. 100,000 n = 6"""
    zeros = ["0" for i in range(n-1)]
    zeros.append("")
    return zeros

if __name__ == '__main__':
    digits = ["1", "4", "7", "2", "1", "2"]
    pprint(get_zeros(len(digits)))