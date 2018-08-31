# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:46:22 2018

122BestTimetoBuyandSellStockII

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

@author: Shanshan
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profits += prices[i]-prices[i-1]
        return profits