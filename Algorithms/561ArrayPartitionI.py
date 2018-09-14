'''
561SArrayPartitionI
Given an array of 2n integers, your task is to group these integers into n pairs
of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi)
for all i from 1 to n as large as possible.
'''


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum_max = 0
        i = 0
        while i < len(nums):
            sum_max += nums[i]
            i = i + 2
        return sum_max
