"""
@title:      31. 下一个排列
@difficulty: 中等
@importance: 5/5
@tags:       分析
"""
from typing import List
from math import inf


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        @tags:              分析
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       见注释
        """
        # 从后向前寻找第一个非递增的下标，改下标即为需交换的第一个下标
        n = len(nums)
        i = n - 2
        while i > -1:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        # special case 反转的情况
        if i == -1:
            return nums.reverse()

        # 寻找 大于 下标i值的 最小的数
        j = i+1
        for k in range(i + 2, n):
            if nums[k] > nums[i] and nums[k] < nums[j]:
                j = k
        # 交换
        nums[i], nums[j] = nums[j], nums[i]

        # i后的数取最小，即排序
        a = sorted(nums[i + 1:])
        for idx in range(i + 1, n):
            nums[idx] = a[idx - i - 1]


Solution().nextPermutation([2, 3, 1])
