"""
@title:      70. 爬楼梯
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        @tags:              递归 斐波那契数列
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       f[i] = f[i-1] + f[i-2]
        """
        @cache
        def dfs(i):
            if i == 1 or i == 2:
                return i

            return dfs(i-1) + dfs(i-2)
        return dfs(n)

    def climbStairs(self, n: int) -> int:
        """
        @tags:              递推dp + 状态压缩
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        a = 1
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
