"""
@title:      62. 不同路径
@difficulty: 简单
@importance: 4/5
@tags:       dp
"""

from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(m*n)
        @space complexity:  O(m*n)
        @description:       一眼dp题，先写出迭代公式 f[i][j] = f[i][j-1] + f[i-1][j]
        """
        f = [[0]*n for i in range(m)]
        for i in range(m):
            f[i][0] = 1
        for i in range(n):
            f[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i][j-1] + f[i-1][j] # 依赖是数据来自 上、左 可以压缩空间复杂度
        return f[m-1][n-1]


Solution().uniquePaths(3, 7)
