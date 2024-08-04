"""
@title:      1289. 下降路径最小和 II
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from math import inf


class Solution:
    """
    状态转移的思路同 leetcode 931，本题的关键在如何快速寻找最小值上
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        @tags:              路径dp + 状态压缩
        @time complexity:   O(n^n)
        @space complexity:  O(n)
        @description:       同leetcode120
        """
        def get2min(arr):
            m = inf
            m_sub = inf
            # 💲计算数组的最小值和次最小值
            for v in arr:
                if v < m:
                    m_sub = m
                    m = v
                elif v < m_sub:
                    m_sub = v
            return m, m_sub

        n = len(grid)
        if n == 1:
            return grid[0][0]

        # 滚动数组优化
        f = [[i for i in grid[0]] for i in range(2)]

        m, m_sub = get2min(grid[0])
        for i in range(1, n):
            cur, pre = i % 2, (i - 1) % 2
            for j in range(n):
                f[cur][j] = (m_sub if f[pre][j] == m else m) + grid[i][j]
            tmp = get2min(f[cur])
            m = tmp[0]
            m_sub = tmp[1]

        return min(f[(n - 1) % 2])
