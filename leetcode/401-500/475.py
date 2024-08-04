"""
name:       475. 供暖器
difficulty: 中等
importance: 5/5
tags:       sort binary_search
"""
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        @tags:              binary_search sort
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       查找每个房子最近的热水器，热水器范围取最大值
        """
        houses.sort()
        heaters.sort()
        res = 0

        for i in houses:
            l = 0
            r = len(heaters)
            # 寻找最近的取暖器 binary_search [left, right)
            while l < r:
                mid = (l + r) // 2
                if heaters[mid] < i:
                    l = mid + 1  # [mid+1, right)
                else:
                    r = mid  # [l, mid)
            # 热水器只在左侧
            if l == len(heaters):
                res = max(res, i - heaters[-1])
            # 热水器只在右侧（或等于右侧）
            elif l == 0:
                res = max(res, heaters[0] - i)
            # 左右侧都有可能
            else:
                res = max(res, min(heaters[l] - i, i - heaters[l - 1]))
        return res
