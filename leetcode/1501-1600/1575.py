"""
@title:      1575. 统计所有可行路径
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from functools import cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
        @tags:              递归
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        """
        MOD = 10**9 + 7

        @cache
        def dfs(i, rest):
            if rest < 0:
                return 0

            return sum(
                0 if i == j else dfs(j, rest - abs(v - locations[i]))
                for j, v in enumerate(locations)
            ) + (1 if i == finish else 0)

        return dfs(start, fuel) % MOD

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
        @tags:              dp递推
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        """
        MOD = 10**9 + 7

        n = len(locations)

        f = [[0]*(n) for _ in range(fuel+1)]
        for i in range(fuel+1):
            f[i][finish] = 1
            for j in range(n):
                for k, v in enumerate(locations):
                    if k != j and i >= abs(locations[j] - v):
                        f[i][j] += f[i-abs(locations[j] - v)][k]
                        f[i][j] %= MOD
        return f[fuel][start]
