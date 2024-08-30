"""
@title:      64. 最小路径和
@difficulty: 简单
@importance: 4/5
@tags:       dp
"""

from typing import List
from math import inf


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(n)
        @description:       路径dp; 带权的 leetcode 62
        """
        n, m = len(grid), len(grid[0])
        f = [inf] * (m + 1)
        f[1] = 0
        for i in range(n):
            for j in range(m):
                f[j + 1] = min(f[j], f[j + 1]) + grid[i][j]
        return f[m]
