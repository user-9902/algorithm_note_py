"""
@title:      673. 最长递增子序列的个数
@difficulty: 中等
@importance: 5/5
@tags:       dp  LIS
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       最长递增子序列求解的过程中，计算以当前元素结尾的最长子序列的个数。greedy的解法相同。
        """
        n = len(nums)
        f = [1] * n
        cnt = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if f[j] + 1 > f[i]:
                        f[i] = f[j] + 1
                        # i能拼到j的结尾 最长子序列个数 = 以j结尾最长子序列的个数
                        cnt[i] = cnt[j]
                    elif f[j] + 1 == f[i]:
                        # 出现新的最长子序列组合 即 i2 能拼接到 j2 的尾部
                        cnt[i] += cnt[j]

        max_l = max(f)
        res = 0
        for i in range(n):
            if f[i] == max_l:
                res += cnt[i]
        return res
