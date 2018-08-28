# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:23:45 2018

14.Longest Common prefix

@author: Shanshan
"""

class Solution:
    def longestCommonPrefix(self,strs):
        '''
        :type strs: List[str]
        :rtype: str
    
        '''
        
        if not strs:
            return ''
        max_idx = min([len(s) for s in strs])
        for i in range(max_idx,0,-1): #backward
            for j in range(1,len(strs)):
                if strs[j][:i] != strs[0][:i]:
                    break
            else:
                return strs[0][:i]
        return ''