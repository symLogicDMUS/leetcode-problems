from pprint import pprint

def sum_int_mags(int_mags):
    sum = 0
    for i in int_mags:
        sum += i
    return sum


if __name__ == '__main__':
    int_mags = [100000, 40000, 7000, 200, 10, 2]
    pprint(sum_int_mags(int_mags))