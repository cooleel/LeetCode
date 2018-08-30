# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:15:25 2018

@author: Shanshan

66PlusOne
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #the idea is adding one to an int
        #change the list to an int
        #add one
        #split the new int to a list meanwhile change str back to int
        new_list = []
        temp = ''.join(str(i) for i in digits)
        temp1 = str(int(temp)+1)
        for i in temp1:
            new_list.append(int(i))
        return new_list