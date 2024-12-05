"""
@title:      3101. 交替子数组计数
@difficulty: 简单
@importance: 4/5
@tags:       滑动窗口
"""
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        res = 0
        for r in range(1, n):
            if nums[r] != nums[r - 1]:
                continue
            else:
                width = r - l
                res += (1 + width) * width // 2
                l = r
        width = n - l
        res += (1 + width) * width // 2
        return res
