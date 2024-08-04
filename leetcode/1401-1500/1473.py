"""
@title:      1473. 粉刷房子 III
@difficulty: 困难
@importance: 4/5
@tags:       序列dp
"""

from typing import List
from math import inf


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        @tags:              序列dp
        @time complexity:   O(mn^2target)
        @space complexity:  O(mntarget)
        @description:       f[i][j][k] 表示前i个元素以颜色j结尾并组成k个分组的最小花费。
                            我们只需处理 f[i] 和 f[i-1] 的关系，见注释
        """

        f = [[[inf] * (target + 1) for _ in range(n + 1)]
             for _ in range(m + 1)]
        for i in range(n + 1):
            f[0][i][0] = 0

        for i in range(m):
            # 当前无需粉刷
            if houses[i] != 0:
                for k in range(1, target + 1):
                    # 遍历前一种颜色
                    for x in range(n + 1):
                        # 和当前颜色相同
                        if x == houses[i]:
                            f[i + 1][houses[i]][k] = min(
                                f[i + 1][houses[i]][k], f[i][x][k]
                            )
                        # 和当前颜色不同
                        else:
                            f[i + 1][houses[i]][k] = min(
                                f[i + 1][houses[i]][k], f[i][x][k - 1]
                            )

            else:
                # 当前选的颜色
                for j in range(1, n + 1):
                    for k in range(1, target + 1):
                        # 前一种颜色
                        for x in range(n + 1):
                            # i-1颜色和i相同
                            if x == j:
                                f[i + 1][j][k] = min(
                                    f[i + 1][j][k], f[i][x][k] + cost[i][j - 1]
                                )
                            # i-1颜色和i不同
                            else:
                                f[i + 1][j][k] = min(
                                    f[i + 1][j][k], f[i][x][k - 1] +
                                    cost[i][j - 1]
                                )
        ans = min(f[m][i][target] for i in range(n + 1))
        return -1 if ans == inf else ans
