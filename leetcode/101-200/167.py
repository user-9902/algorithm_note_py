"""
@title:      167. 两数之和 II - 输入有序数组
@difficulty: 简单
@importance: 4/5
@tags:       指针
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        @tags:              双指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       利用有序性，指针相向而行
        """
        n = len(numbers)
        p1 = 0
        p2 = n-1
        while p1 < p2:
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
        return []
