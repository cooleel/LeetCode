# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:15:54 2018

@author: Shanshan


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


"""

class solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for num_inx,num in enumerate(nums):
            if target-num in dic:
                return dic[target-num],num_inx
            dic[num] = num_inx