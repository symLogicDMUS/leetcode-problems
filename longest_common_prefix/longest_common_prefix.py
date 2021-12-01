import sys


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 1:
        return strs[0]
    strs = sorted(strs, key=len)
    n = len(strs[0])
    answer = ""
    for i in range(n):
        sub_strs = map(lambda s: s[0:i + 1], strs)
        if all(ele == sub_strs[0] for ele in sub_strs):
            answer = sub_strs[0]
    return answer

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/longest-common-prefix/ """
    longest_common_prefix(sys.argv[1:])