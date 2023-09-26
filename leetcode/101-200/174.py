"""
174. 地下城游戏
dp; dfs
dp[0][0] 最少剩余生命值
需要注意：当前剩余生命值至少为1
"""

from typing import List
from math import inf


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        dp
        dp[i][j] 表示在i行j列能拯救公主的最少生命值
        dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]), 1)
        """
        n = len(dungeon)
        m = len(dungeon[0])
        f = [[0]*m for i in range(n)]

        f[-1][-1] = 1 if dungeon[-1][-1] > 0 else -dungeon[-1][-1] + 1

        for i in range(n-2, -1, -1):
            f[i][m-1] = max(f[i+1][m-1] - dungeon[i][m-1], 1)
        for i in range(m-2, -1, -1):
            f[n-1][i] = max(f[n-1][i+1] - dungeon[n-1][i], 1)

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                f[i][j] = max(min(f[i+1][j], f[i][j+1]) - dungeon[i][j], 1)
        return f[0][0]

    def calculateMinimumHP2(self, dungeon: List[List[int]]) -> int:
        """
        dp
        显然上面的dp能压缩为一维滚动数组
        """

        n = len(dungeon)
        m = len(dungeon[0])
        # 初始化状态
        f = [0] * m
        f[-1] = 1 if dungeon[-1][-1] > 0 else -dungeon[-1][-1] + 1
        for i in range(m-2, -1, -1):
            f[i] = max(1, f[i+1] - dungeon[-1][i])
        # 递推
        for i in range(n-2, -1, -1):
            for j in range(m-1, -1, -1):
                f[j] = max(1, min(f[j], inf if j == m - 1 else f[j+1])
                           - dungeon[i][j])
        return f[0]


Solution().calculateMinimumHP2([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
