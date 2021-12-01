__doc__ = \
"""
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900
"""

mapping = {
    "IIII": "IV",
    "IVI": "V",
    "VIIII": "IX",
    "IXI": "X",
    "XXXX": "XL",
    "XLX": "L",
    "LXXXX": "XC",
    "XCX": "C",
    "CCCC": "CD",
    "CDC": "D",
    "DCCCC": "CM",
    "CMC": "M",
}