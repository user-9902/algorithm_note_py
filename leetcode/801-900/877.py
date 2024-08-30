"""
@title:      877. 石子游戏
@difficulty: 中等
@importance: 0/5    同leetcode 486
@tags:       区间dp 前缀和 博弈
"""
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        @tags:              区间dp 前缀和              
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        """
        n = len(piles)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + piles[i]

        # 区间dp
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = piles[i]
            for j in range(i + 1, n):
                f[i][j] = max(
                    piles[i] + pre[j + 1] - pre[i + 1] - f[i + 1][j],
                    piles[j] + pre[j] - pre[i] - f[i][j - 1],
                )
        return f[0][n - 1] > pre[n] / 2
