"""
@title:      122. 买卖股票的最佳时机 II
@difficulty: 中等
@importance: 4/5
@tags:       dp, greedy
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)    f[i] 状态只与 f[i-1] 有关 可以压缩至一维
        @description:       每天可以持有或不持有
        """
        n = len(prices)
        f1 = [0] * n  # 手上没有股票
        f2 = [0] * n  # 手上有股票
        f2[0] = -prices[0]

        for i in range(1, n):
            # 继续不持有 卖掉持有的
            f1[i] = max(f1[i - 1], f2[i - 1] + prices[i])
            # 继续持有  买入
            f2[i] = max(f2[i - 1], f1[i - 1] - prices[i])
        return f1[n - 1]

    def maxProfit(self, prices: List[int]) -> int:
        """
        @tags:              greedy
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       不限买卖次数，天数，收割正利润即可
        """
        n = len(prices)
        res = 0
        for i in range(1, n):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
