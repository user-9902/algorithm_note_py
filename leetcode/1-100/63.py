"""
@title:      63. 不同路径 II
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from math import inf


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        @tags:              dp
        @time complexity:   O(m*n)
        @space complexity:  O(m*n)
        @description:       同 62 障碍物是无法到达的，设为其状态值保持为0即可。障碍的处理较繁杂
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        f = [[0] * n for i in range(m)]
        # 第一列是否都能到达
        for i in range(m):
            if i > 0 and obstacleGrid[i - 1][0] == 1:
                break
            f[i][0] = 1
        # 第一行是否都能到达
        for i in range(n):
            if i > 0 and obstacleGrid[0][i - 1] == 1:
                break
            f[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                a = f[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0
                b = f[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0
                f[i][j] = a + b

        return f[m - 1][n - 1]
