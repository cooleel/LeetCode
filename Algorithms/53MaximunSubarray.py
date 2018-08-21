# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:00:14 2018

@author: Shanshan


53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.


"""

def maxSubArray(nums):
    '''
    :type nums: List[int]
    :rtype: int
    
    '''
    for i in range(1, len(nums)):

        if nums[i-1] > 0 :
            nums[i] += nums[i-1]

    return max(nums)
