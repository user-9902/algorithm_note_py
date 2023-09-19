"""
494. 目标和
01背包变形题

假设目标解为x, sum(list)为sum
x - (sum - x) = target
2x = sum + target
x = (sum + target) / 2
问题就变为从nums找寻和为x的解
"""

from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        递推
        f[i][c] = f[i-1][c] + f[i-1][c-nums[i]]
                    当前数字不选 + 选择当前数字
        """
        target += sum(nums)
        # num 都为正整数，下列情况无解
        if target < 0 or target % 2:
            return 0
        target >>= 1

        f = [0]* (target + 1) # 防止越界加一
        f[0] = 1 # 初始状态

        for x in nums:
            for c in range(target, x-1, -1):
                    f[c] = f[c] + f[c-x]
        
        return f[target]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
        递归
        """
        target += sum(nums)
        # num 都为正整数，下列情况无解
        if target < 0 or target % 2:
            return 0
        target >>= 1

        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i-1, c)
            # 选或者不选
            return dfs(i-1, c) + dfs(i-1, c - nums[i])

        return dfs(n-1, target)
