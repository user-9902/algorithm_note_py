"""
name:       81. 搜索旋转排序数组 II
difficulty: 中等
importance: 5/5
tags:       二分
"""

from typing import List
from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        @tags:              二分
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       leetcode 33 进阶
        """
        n = len(nums)
        l = 0
        r = n - 1
        # 这一步非常重要 排除了 如果左端点 和 右端点相同，则无法找到最低点。
        while l <= r and nums[l] == nums[r]:
            l += 1
        # 找到最低点
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[n - 1]:
                l = mid + 1
            else:
                r = mid

        if target > nums[n - 1]:
            idx = bisect_left(nums, target, hi=r - 1)
        else:
            idx = bisect_left(nums, target, lo=r)
        return idx <= n - 1 and target == nums[idx]
