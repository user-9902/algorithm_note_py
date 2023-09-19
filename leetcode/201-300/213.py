"""
213. 打家劫舍 II
同打家劫舍Ⅰ
因为形成了环，这里考虑从节点一进行切割
既分别考虑，选择第一家，不选择第一家的情况
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        # dp[0] 不选择第一家 dp[1] 选第一家
        dp = [nums[1], max(nums[1], nums[2])]
        for i in range(3, n):
            dp.append(max(dp[-2] + nums[i], dp[-1]))

        dp2 = [nums[0], nums[0]]
        for i in range(2, n-1):
            dp2.append(max(dp2[-2] + nums[i], dp2[-1]))

        return max(dp[-1], dp2[-1])


Solution().rob([1, 2, 1, 1])
