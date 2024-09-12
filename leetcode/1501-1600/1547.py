"""
@title:      1547. 切棍子的最小成本
@difficulty: 中等
@importance: 4/5
@tags:       记忆化搜索 二分
"""
from typing import List
from functools import cache
from bisect import bisect_left, bisect_right
from math import inf


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        @tags:              记忆化搜索 二分
        @time complexity:   O(m^2 * log m)
        @space complexity:  O(m^2)
        """
        cuts.sort()

        # 划分子问题，切割区间 (l,r)
        @cache
        def dfs(l, r):
            res = inf
            # 寻找分割点左右边界
            left = bisect_left(cuts, l + 1)
            right = bisect_right(cuts, r - 1)
            for i in range(left, right):
                res = min(res, dfs(l, cuts[i]) + dfs(cuts[i], r) + r - l)
            return 0 if res == inf else res

        return dfs(0, n)


Solution().minCost(7, [0, 1, 3, 4, 5, 7])
