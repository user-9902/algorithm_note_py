"""
@title:      1712. 将数组分成三个子数组的方案数
@difficulty: 中等
@importance: 5/5
@tags:       前缀和 二分
"""
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        @tags:              前缀和
        @time complexity:   O(nlogn)   
        @space complexity:  O(n)
        @description:       前缀和 确认区间
        """
        MOD = 10**9 + 7

        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        total = pre[n]
        max_l = total // 3

        ans = 0
        # 枚举第一个区间 至少留两个区间给 中间 和后面
        for i in range(1, n - 1):
            # 左侧不能超过sum的三分之一
            if pre[i] > max_l:
                break
            # left <= mid <= right
            max_m = ((total - pre[i]) // 2) + pre[i]
            # 💲二分边界场景要熟悉 = < <= > >=   bisect_left 第一个 >= target的下标  bisect_right 第一个 > target的下标
            # 二分查找 >= pre[i]
            idx1 = bisect_left(pre, pre[i] * 2, lo=i + 1)
            # 二分查找 <= max_m
            idx2 = bisect_left(pre, max_m + 1, hi=n) - 1
            ans = (ans + idx2 - idx1 + 1) % MOD

        return ans
