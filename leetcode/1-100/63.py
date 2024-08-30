"""
@title:      63. 不同路径 II
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(n)
        @description:       同 62 障碍物是无法到达的，设为其状态值保持为0即可。
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        # 💲一般化特殊情况。这里第一行第一列为特殊情况，没有上侧或左侧，我们为其补一行一列，使得特殊值不再特殊，类似一些链表题中头节点的处理。
        f = [0] * (m + 1)
        f[1] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    # 上侧路径 + 左侧路径
                    f[j + 1] += f[j]
                else:
                    # 当前为障碍物 不可到达
                    f[j + 1] = 0
        return f[m]
