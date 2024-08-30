"""
@title:      35. 搜索插入位置
@difficulty: 简单
@importance: 5/5
@tags:       二分基础
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        @tags:              二分
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       题目要寻找 <= target的下标
        """
        n = len(nums)
        l = 0
        r = n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
