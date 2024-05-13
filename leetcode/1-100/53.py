"""
53. 最大子数组和
dp; 分治; greedy
"""
from typing import List
from math import inf
from functools import cache


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        由于连续性，要么加入前缀和，要么单独组成子数组
        """
        n = len(nums)
        f = [0 for _ in range(n+1)]
        f[0] = -inf

        for i in range(1, n+1):
            f[i] = max(f[i-1]+nums[i-1], nums[i-1])

        return max(f)

        # 空间优化
        # n = len(nums)
        # pre = ans = nums[0]
        # for i in range(1, n):
        #     pre = max(pre + nums[i], nums[i])
        #     ans = max(ans, pre)
        # return ans

    def maxSubArray2(self, nums: List[int]) -> int:
        """
        分治
        """
        @cache
        def dfs(l, r):
            if l + 1 == r:
                return nums[l]
            m = (l+r) >> 1
            return max(dfs(l, m), dfs(m, r), dfs(l, m) + dfs(m, r))

        print(dfs(0, len(nums)))
        return dfs(0, len(nums))

    def maxSubArray3(self, nums: List[int]) -> int:
        """
        greedy
        """
        pass


Solution().maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4])
