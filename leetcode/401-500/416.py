"""
@title:      416. 分割等和子集
@difficulty: 简单
@importance: 4/5
@tags:       dp
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        @tags:              dp
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       01背包
        """
        sum_n = sum(nums)
        if sum_n % 2:
            return False
        target = sum_n >> 1
        n = len(nums)
        f = [[0]*(target+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(1, target+1):
                # 不选
                f[i+1][j] = f[i][j]
                # 选
                if j >= nums[i]:
                    f[i+1][j] = max(f[i+1][j], f[i][j-nums[i]] + nums[i])
        return f[n][target] == target
