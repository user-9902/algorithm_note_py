"""
@title:      322. 零钱兑换
@difficulty: 中等
@importance: 5/5
@tags:       greedy
"""

from typing import List
from functools import cache
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(nk)
        @space complexity:  O(nk)
        @description:       完全背包
        """
        @cache
        def dfs(i, n):
            if n == 0:
                return 0
            if n < 0:
                return inf
            if i == 0:
                return dfs(i, n - coins[i]) + 1
            return min(dfs(i - 1, n), dfs(i, n - coins[i]) + 1)

        ans = dfs(len(coins) - 1, amount)
        return -1 if ans == inf else ans

    def coinChange(self, coins: List[int], m: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(nk)
        @space complexity:  O(nk)
        @description:       完全背包
        """
        n = len(coins)

        f = [[inf] * (m + 1) for _ in range(n + 1)]
        f[0][0] = 0

        for i in range(n):
            for j in range(m + 1):
                # 当前不选
                f[i + 1][j] = f[i][j]
                # 当前选
                if j >= coins[i]:
                    f[i + 1][j] = min(f[i + 1][j], f[i+1][j - coins[i]] + 1)
        return -1 if f[n][m] == inf else f[n][m]

    def coinChange(self, coins: List[int], m: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(nk)
        @space complexity:  O(k)
        @description:       空间压缩
        """
        n = len(coins)

        f = [inf] * (m + 1)
        f[0] = 0

        for i in range(n):
            for j in range(coins[i], m + 1):
                f[j] = min(f[j], f[j - coins[i]] + 1)
        return -1 if f[m] == inf else f[m]
