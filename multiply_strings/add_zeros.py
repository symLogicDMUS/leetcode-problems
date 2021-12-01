from typing import List


def add_zeros(digits: List[str], zeros: List[str]):
    for i in range(len(digits)):
        digits[i] += "".join(zeros)
        zeros.pop(0)
    return digits

if __name__ == '__main__':
    digits = ["1", "4", "7", "2", "1", "2"]  # 147,212
    zeros = ["0", "0", "0", "0", "0", ""]
    print(add_zeros(digits, zeros))