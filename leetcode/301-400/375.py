"""
@title:      375. 猜数字大小 II
@difficulty: 中等
@importance: 5/5
@tags:       记忆化搜索 dp
"""
from functools import cache
from math import inf


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(n^2)   
        @space complexity:  O(n^2)  隐形的调用栈的开销会比较大,栈的深度为O(n)
        """
        @cache
        def dfs(l, r):
            if l >= r:
                return 0
            res = inf
            # 遍历i，找最小保证能赢的花费
            for i in range(l, r + 1):
                # 选i时计算最大花费保证能赢
                res = min(res, max(dfs(l, i - 1), dfs(i + 1, r)) + i)
            return res

        return dfs(0, n)

    def getMoneyAmount(self, n: int) -> int:
        """
        @tags:              区间dp
        @time complexity:   O(n^2)   
        @space complexity:  O(n^2)
        @description:       f[i][j] 表示 猜测范围为i-j 时的最小花费
        """
        f = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = inf
                for k in range(i, j):
                    f[i][j] = min(f[i][j], max(f[i][k - 1], f[k + 1][j]) + k)
        return f[1][n]
