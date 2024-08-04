"""
27. 移除元素
difficulty: 简单
importance: 4/5
tags:       指针
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0
        for i, v in enumerate(nums):
            while s < i and nums[s] != val:
                s += 1
            if v != val:
                nums[i], nums[s] = nums[s], nums[i]
                s += 1
        return s
