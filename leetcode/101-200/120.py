"""
@title:      120. 三角形最小路径和
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

from typing import List
from functools import cache
from math import inf


class Solution:
    """
    三十年前的奥赛，如今的入门
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        @tags:              递归
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       路径dp
        """
        n = len(triangle)

        @cache
        def dfs(i, j):
            if i == n:
                return 0

            return min(
                dfs(i + 1, j) + triangle[i][j],
                dfs(i + 1, j + 1) + triangle[i][j]
            )

        return dfs(0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        @tags:              dp递推 + 状态压缩
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        """
        n = len(triangle)
        f = [inf] * (n + 1)
        f[1] = triangle[0][0]

        for i in range(1, n):
            # 状态来自上方 上左方 防止覆盖从后向前遍历
            for j in range(i, -1, -1):
                f[j + 1] = min(
                    f[j + 1] + triangle[i][j],
                    f[j] + triangle[i][j]
                )
        return min(f)
