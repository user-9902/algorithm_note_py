"""
377. 组合总和 Ⅳ
difficulty: 中等
importance: 4/5
tags:       dp
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        类似完全背包
        """
        dp = [1] + [0] * target

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]
