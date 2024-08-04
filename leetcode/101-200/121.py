"""
@title:      买卖股票的最佳时机 I
@difficulty: 简单
@importance: 3/5
@tags:       
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(1)    
        @description:       前缀最小值
        """
        minv = prices[0]
        res = 0
        for v in prices:
            if v - minv > res:
                res = v - minv
            if v < minv:
                minv = v
        return res
