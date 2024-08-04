"""
@title:      123. 买卖股票的最佳时机 III
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        @tags:              dp 状态压缩
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       见leetcode122
        """
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])            # 一次买找最低点
            sell1 = max(sell1, buy1 + prices[i])    # 一次卖找最高点
            buy2 = max(buy2, sell1 - prices[i])     # 第二次买的低点
            sell2 = max(sell2, buy2 + prices[i])    # 第二次卖的高点

        return sell2
