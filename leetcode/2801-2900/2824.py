"""
@title:      2824. 统计和小于目标的下标对数目
@difficulty: 简单
@importance: 4/5
@tags:       sort
"""
from typing import List
import bisect


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        @tags:              bf
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       暴力枚举
        """
        ans = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans

    def countPairs(self, nums: List[int], target: int) -> int:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       题目等价于 两数之和是否<target 排序+二分即可
        """
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n - 1):
            t = target - nums[i]
            r = bisect.bisect_left(nums, t) - 1
            if r > i:
                ans += r - i
        return ans
