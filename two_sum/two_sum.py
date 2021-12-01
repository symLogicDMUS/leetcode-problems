import sys

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        if i != len(nums) - 1 and nums[i] + nums[i + 1] == target:
            return [i, i + 1]
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

if __name__ == '__main__':
    """ Problem URL: https://leetcode.com/problems/two-sum/ """
    two_sum(sys.argv[1], int(sys.argv[2]))