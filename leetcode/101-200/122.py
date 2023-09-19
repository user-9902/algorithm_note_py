"""
122. 买卖股票的最佳时机 II
dp; greedy
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp
        每天有两种状态，手里有股票或手里没股票
        0 表示手中没有股票 1 表示手中有股票
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        dp[i][0] 第i天手上没股票时最大值，继续不持有，或者前一天卖出的
        dp[i][1] 第i天手上有股票时最大值，继续持有的，或者前一天买入的
        """
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        """
        greedy
        收割正利润
        最大利润，即收集每天的正利润
            若连续多天正利润，如 a a+1 a+2天间连续正利润，则a买入a-2卖出
            若非连续正利润，如 a a+1天之间出现出现正利润，则a买入 a+1卖出
        局部最优解和全局最优解是不冲突的
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                res += prices[i] - prices[i - 1]
        return res
