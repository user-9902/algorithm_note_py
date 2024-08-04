"""
26. 删除有序数组中的重复项
difficulty: 简单
importance: 4/5
tags:       指针
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        for i, v in enumerate(nums):
            if v > nums[s]:
                s += 1
                nums[i], nums[s] = nums[s], nums[i]
        return s + 1
