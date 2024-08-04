"""
@title:      799. 香槟塔
@difficulty: 简单
@importance: 3/5
@tags:       dp 模拟
"""

from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       模拟下溢的过程
        """
        n = 10
        f = [[0] * n for _ in range(n)]
        f[0][0] = poured
        for i in range(n):
            for j in range(i+1):
                if f[i][j] > 1:
                    f[i + 1][j] += (f[i][j] - 1) / 2
                    f[i + 1][j + 1] += (f[i][j] - 1) / 2
                    f[i][j] = 1
        return f[query_row][query_glass] / 1
