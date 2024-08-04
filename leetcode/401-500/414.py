"""
@title:      414. 第三大的数
@difficulty: 简单
@importance: 4/5
@tags:       sort
"""
from typing import List
from sortedcontainers import SortedSet


class Solution:
    """
    类排序算法、一次遍历+三变量记录、排序等都可以解决
    """

    def thirdMax(self, nums: List[int]) -> int:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(nlogn)
        @description:       排序完后，查找第3大的数
        """
        nums.sort()
        n = len(nums)
        k = 2

        for i in range(n-2, -1, -1):
            if (nums[i] < nums[i+1]):
                k -= 1
                if (k == 0):
                    return nums[i]
        return nums[n-1]

    def thirdMax(self, nums: List[int]) -> int:
        """
        @tags:              优先队列
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       这里优化了空间复杂度
        """
        s = SortedSet()
        for num in nums:
            s.add(num)
            if len(s) > 3:
                s.pop(0)
        return s[0] if len(s) == 3 else s[-1]
