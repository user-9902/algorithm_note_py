"""
@title:      688. 骑士在棋盘上的概率
@difficulty: 简单
@importance: 4/5
@tags:       记忆化搜索 dp
"""
from typing import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
        @tags:              dp
        @time complexity:   O(k*n^2)   
        @space complexity:  O(n^2)
        """
        @cache
        def dfs(row, column, k):
            condition = 0 <= row <= n - 1 and 0 <= column <= n - 1
            if k == 0:
                return 1 if condition else 0

            if condition:
                return (
                    dfs(row - 1, column - 2, k - 1)
                    + dfs(row - 1, column + 2, k - 1)
                    + dfs(row + 1, column - 2, k - 1)
                    + dfs(row + 1, column + 2, k - 1)
                    + dfs(row - 2, column - 1, k - 1)
                    + dfs(row - 2, column + 1, k - 1)
                    + dfs(row + 2, column - 1, k - 1)
                    + dfs(row + 2, column + 1, k - 1)
                )
            else:
                return 0
        # 能保留在棋盘上的数量 / 总的可能性
        return dfs(row, column, k) / 8**k
