"""
188. 买卖股票的最佳时机 IV
dp
leetcode 122的变形题 加上了天数限制
"""
from typing import List
from math import inf


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        f[i][j][0] 表示第i天第j手交易当前不持有股票时的最大收益
        f[i][j][1] 手头持有时的最大收益
            f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1] + price)
            f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0] - price)
        """
        n = len(prices)
        # k + 2 i + 1 都是为了防止状态转移方程导致数组越界
        # 初始状态只有：第1天不持有是合法的
        f = [[[-inf, -inf] for _ in range(k+2)] for _ in range(n+1)]

        for i in range(1, k+2):
            f[0][i][0] = 0

        for i, p in enumerate(prices):
            for j in range(k+1):
                f[i+1][j+1][0] = max(f[i][j+1][0], f[i][j+1][1] + p)
                f[i+1][j+1][1] = max(f[i][j+1][1], f[i][j][0] - p)

        return f[-1][-1][0]

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        """
        空间优化
        上面的状态转移方程中i是可以去掉的因为 f[i] 只与f[i-1]相关4
        j从后向前枚举即可
        """
        f = [[-inf, -inf] for _ in range(k+2)]

        for i in range(1, k+2):
            print(f)
            f[i][0] = 0

        for _, p in enumerate(prices):
            for j in range(k, -1, -1):
                f[j+1][0] = max(f[j+1][0], f[j+1][1] + p)
                f[j+1][1] = max(f[j+1][1], f[j][0] - p)

        print(f)
        return f[-1][0]


Solution().maxProfit2(2, [3, 3, 5, 0, 0, 3, 1, 4])
