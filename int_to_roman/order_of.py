def order_1(d):
    return "I" * d


def order_10(d):
    return "X" * d


def order_100(d):
    return "C" * d


def order_1000(d):
    return "M" * d

def order_1_adjust(r: str):
    if "IIII" in r:
        r = r.replace("IIII", "IV", 1)
    if "IVI" in r:
        r = r.replace("IVI", "V", 1)
    if "VIIII" in r:
        r = r.replace("VIIII", "IX", 1)
    return r

def order_10_adjust(r: str):
    if "XXXX" in r:
        r = r.replace("XXXX", "XL", 1)
    if "XLX" in r:
        r = r.replace("XLX", "L", 1)
    if "LXXXX" in r:
        r = r.replace("LXXXX", "XC", 1)
    return r

def order_100_adjust(r: str):
    if "CCCC" in r:
        r = r.replace("CCCC", "CD", 1)
    if "CDC" in r:
        r = r.replace("CDC", "D", 1)
    if "DCCCC" in r:
        r = r.replace("DCCCC", "CM", 1)
    return r