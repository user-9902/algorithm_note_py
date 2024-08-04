"""
@title:      931. 下降路径最小和
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from math import inf


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        @tags:              路径dp + 状态压缩
        @time complexity:   O(n^n)
        @space complexity:  O(n)
        @description:       同leetcode120
        """
        n = len(matrix)
        # 由于 f[i] 来自上方 上左方 上右方，为防止覆盖，这里需要滚动数组来压缩
        f = [[inf] + matrix[0][:] + [inf] for _ in range(2)]

        for i in range(1, n):
            for j in range(n):
                cur, pre = i % 2, (i - 1) % 2
                f[cur][j + 1] = (
                    min(f[pre][j], f[pre][j + 1], f[pre][j + 2]) + matrix[i][j]
                )

        return min(f[(n - 1) % 2])
