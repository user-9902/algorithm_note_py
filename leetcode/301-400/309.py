"""
309. 买卖股票的最佳时机含冷冻期
dp
leetcode122的变形题
"""

from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        f = [[0, 0] for _ in range(n+2)]
        f[0][1] = -inf
        f[1][1] = -inf

        for i in range(n):
            # 不持有
            f[i+2][0] = max(f[i+1][0], f[i+1][1] + prices[i])
            # 持有
            f[i+2][1] = max(f[i+1][1], f[i][0] - prices[i])
        return f[-1][0]


Solution().maxProfit([1, 2, 3, 0, 2])
