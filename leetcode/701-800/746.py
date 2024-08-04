"""
@title:      746. 使用最小花费爬楼梯
@difficulty: 简单
@importance: 5/5
@tags:       dp
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       先写出迭代公式 c[n] = min(c[n-1], c[n-2]) + cost[i]
        """
        # 注意可以 "跨上" 最后一级台阶，也可以 "跨过" 最后一级台阶
        cost.append(0)
        n = len(cost)
        f = [0] * n
        f[0] = cost[0]
        f[1] = cost[1]
        for i in range(2, n):
            f[i] = min(f[i - 1], f[i - 2]) + cost[i]
        return f[n-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        @tags:              dp + 优化空间复杂度
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       同斐波那契额数列 我们只依赖前两种状态
        """
        n = len(cost)
        f = [cost[0], cost[1]]
        for i in range(2, n):
            f[i % 2] = min(f) + cost[i]
        return min(f)
