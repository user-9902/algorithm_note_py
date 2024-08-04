"""
name:       448. 找到所有数组中消失的数字
difficulty: 简单
importance: 3/5
tags:       hashmao
"""
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       hashmap 记录数字出现与否
        """
        n = len(nums)
        s = [i for i in range(1, n + 1)]

        for v in nums:
            if 0 < v < n + 1:
                s[v - 1] = 0

        return list(filter(lambda x: x != 0, s))

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       使用负号作为标记以减少额外空间 见leetcode41
        """
        n = len(nums)

        for v in nums:
            i = abs(v)
            if 0 < i < n + 1:
                nums[i - 1] = -abs(nums[i - 1])

        res = []
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i + 1)
        return res

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        @tags:              sort swap
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       将每个元素交换至正确位置 交换的思路见leetcode41
        """
        n = len(nums)

        for i in range(n):
            v = nums[i]
            while (
                0 < v < n+1
                and v != i + 1
                and v != nums[v - 1]
            ):
                nums[i],  nums[v - 1] = nums[v - 1], nums[i]
                v = nums[i]
        res = []
        for i, v in enumerate(nums):
            if v != i + 1:
                res.append(i + 1)
        return res
