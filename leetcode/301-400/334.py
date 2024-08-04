"""
@title:      334. 递增的三元子序列
@difficulty: 中等
@importance: 4/5
@tags:       LIS dp
"""

from bisect import bisect_left
from typing import List
from math import inf


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        @title:             LIS
        @time complexity:   O(nlogn)
        @space complexity:  O(n)  
        @tags:              最长递增子序列的长度是否大于等于3
        """
        stack = []
        for i, v in enumerate(nums):
            if not stack:
                stack.append(v)
            else:
                if v > stack[-1]:
                    stack.append(v)
                else:
                    idx = bisect_left(stack, v)
                    stack[idx] = v

        return len(stack) > 2

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        @title:             LIS
        @time complexity:   O(n)
        @space complexity:  O(1)  
        @tags:              LIS优化 只需维护长度为3的数组
        """
        stack = [inf]*3
        for i, v in enumerate(nums):
            if v <= stack[0]:
                stack[0] = v
            elif v <= stack[1]:
                stack[1] = v
            else:
                return True
        return False
