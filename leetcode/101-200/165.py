"""
167. 两数之和 II - 输入有序数组
双指针
利用有序性，相向双指针
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
