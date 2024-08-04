"""
@title:      279. 完全平方数
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from math import inf

nums = [i * i for i in range(101)]


class Solution:
    def numSquares(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(nk)
        @space complexity:  O(n)
        @description:       完全背包 见leetcode322
        """
        f = [inf] * (n+1)
        f[0] = 0
        for _, x in enumerate(nums):
            for j in range(x, n+1):
                f[j] = min(f[j], f[j-x] + 1)
        return f[n]
