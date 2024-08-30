"""
@title:      34. 在排序数组中查找元素的第一个和最后一个位置
@difficulty: 中等
@importance: 5/5
@tags:       二分
"""
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        @tags:              二分
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       需熟悉二分 > >= < <=的写法
        """
        i = bisect_left(nums, target)
        if i == len(nums) or nums[i] != target:
            return [-1, -1]
        else:
            i2 = bisect_right(nums, target)
            return [i, i2 - 1]
