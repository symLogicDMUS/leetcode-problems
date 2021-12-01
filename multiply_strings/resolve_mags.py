from pprint import pprint
from multiply_strings.digits import digits

def resolve_mag(mag):
    if len(mag) == 1:
        return digits[mag]
    str_lead_d = mag[0]
    int_lead_d = digits[str_lead_d]
    z_count = mag.count("0")
    return int_lead_d * 10 ** z_count

def resolve_mags(mags):
    """convert string mags to int mags"""
    for i in range(len(mags)):
        mags[i] = resolve_mag(mags[i])
    return mags

if __name__ == '__main__':
    mags = ['100000', '40000', '7000', '200', '10', '2']
    pprint(resolve_mags(mags))