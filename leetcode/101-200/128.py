"""
@title:      128. 最长连续序列
@difficulty: 中等
@importance: 4/5
@tags:       并查集 hashmap
"""

from functools import cache
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        @tags:              并查集
        @time complexity:   O(α(n))    ❌ 题目要求的复杂度为O(n)
        @space complexity:  O(n)
        @description:       并查集模板
        """
        pass

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       依然是并查集的思路，见注释
        """
        map = {}
        ans = 0
        for i in nums:
            if i not in map:
                l = r = i   # 左右边界 [l,r]
                a = b = False   # 左右边界是否变化
                if i + 1 in map:
                    r = map[i + 1][1]
                    a = True
                if i - 1 in map:
                    l = map[i - 1][0]
                    b = True
                ans = max(ans, r - l + 1)
                map[i] = [l, r]
                # 能组成更大的区间，则将被合并区间边界的元素都指向更大的新区间，即并查集中合并入一个区间内。
                if a:
                    if map[i + 1][0] in map:
                        map[map[i + 1][0]] = map[i]
                    if map[i + 1][1] in map:
                        map[map[i + 1][1]] = map[i]
                    map[i + 1] = map[i]
                if b:
                    if map[i - 1][0] in map:
                        map[map[i - 1][0]] = map[i]
                    if map[i - 1][1] in map:
                        map[map[i - 1][1]] = map[i]
                    map[i - 1] = map[i]
        return ans
