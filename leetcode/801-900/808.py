"""
@title:      808. 分汤
@difficulty: 简单
@importance: 4/5
@tags:       dp
"""
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        """
        @tags:              dp 💲浮点精度
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        """
        n = (n + 24) // 25
        if n >= 179:        # 题目的数据量很大，导致我们需要写出这个特例，由于浮点精度问题，这里的结论是成立的
            return 1.0

        @cache
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (
                dfs(a - 4, b)
                + dfs(a - 3, b - 1)
                + dfs(a - 2, b - 2)
                + dfs(a - 1, b - 3)
            ) / 4

        return dfs(n, n)
