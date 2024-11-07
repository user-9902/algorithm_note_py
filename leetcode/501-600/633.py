"""
@title:      633. 平方数之和
@difficulty: 简单
@importance: 3/5
@tags:       双指针
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        @tags:              sort dp
        @time complexity:   O(√n)
        @space complexity:  O(√n)   #空间复杂度可优化掉
        @description:       朴素枚举
        """
        s = set()
        i = 0
        while i * i <= c:
            target = c - i * i
            if target in s or target == i * i:
                return True
            s.add(i * i)
            i += 1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        """
        @tags:              sort dp
        @time complexity:   O(√n)
        @space complexity:  O(1)
        @description:       双指针
        """
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            sum = left * left + right * right
            if sum == c:
                return True
            if sum > c:
                right -= 1
            else:
                left += 1
        return False
