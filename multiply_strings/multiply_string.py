import sys

from multiply_strings.resolve_number import resolve_number


def multiply(num1, num2) -> str:
    """
    multiply 2 numbers passed as strings without using built in libraries to convert string to int.
    return the result as a string
    """
    int_num1 = resolve_number(num1)
    int_num2 = resolve_number(num2)
    return str(int_num1 * int_num2)

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/multiply-strings/ """
    print("{} * {} = ".format(sys.argv[1], sys.argv[2]), multiply(sys.argv[1], sys.argv[2]))