"""
@title:      413. 等差数列划分
@difficulty: 简单
@importance: 3/5
@tags:       滑动窗口 等差数列
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        @tags:              滑动窗口
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       保证窗口内的数组为等差数组，如何通过等差数列求和公式计算数量
        """
        l = 0
        n = len(nums)
        if n < 3:
            return 0

        pre_gap = nums[1] - nums[0]
        res = 0
        for i in range(2, n):
            gap = nums[i] - nums[i - 1]
            if gap == pre_gap:
                continue
            else:
                if i - l >= 3:
                    res += (i - l - 2) * (i - l - 1) // 2
                l = i - 1
                pre_gap = gap
        if n - l >= 3:
            res += (i - l - 1) * (i - l) // 2
        return res


Solution().numberOfArithmeticSlices([1, 2, 3, 4])
