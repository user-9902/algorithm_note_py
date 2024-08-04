"""
@title:      2304. 网格中的最小路径代价
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        """
        @tags:              路径dp + 状态压缩
        @time complexity:   O(n^n)
        @space complexity:  O(n)
        @description:       leetcode 1289 的简化版本
        """
        n, m = len(grid), len(grid[0])
        f = [[0] * m for _ in range(2)]

        for i in range(1, n):
            pre = (i-1) % 2
            cur = i % 2
            for j in range(m):
                f[cur][j] = min(
                    f[pre][k] + moveCost[grid[i - 1][k]][j] + grid[i - 1][k]
                    for k in range(m)
                )

        return min(f[(n - 1) % 2][i] + grid[n - 1][i] for i in range(m))
