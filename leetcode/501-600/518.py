"""
@title:      518. 零钱兑换 II
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

from typing import List
from functools import cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        @tags:              递归
        @time complexity:   O(nk)
        @space complexity:  O(nk)
        @description:       完全背包 同 leetcode322
        """
        @cache
        def dfs(i, amount):
            if i < 0:
                return 1 if amount == 0 else 0
            if amount < coins[i]:
                return dfs(i - 1, amount)
            return dfs(i - 1, amount) + dfs(i, amount - coins[i])

        return dfs(len(coins) - 1, amount)
