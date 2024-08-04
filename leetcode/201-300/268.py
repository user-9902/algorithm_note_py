"""
name:       268. 丢失的数字
difficulty: 1/5
importance: 3/5
tags:       sort math 位运算
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(1)
        @description:
        """
        nums.sort()
        for i, v in enumerate(nums):
            if v > i:
                return i
        return len(nums)

    def missingNumber(self, nums: List[int]) -> int:
        """
        @tags:              math
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       0-n的和为 n*(n+1)/2
        """
        n = len(nums)
        sum_nums = sum(nums)
        sum_n = n*(n+1)//2
        return sum_n - sum_nums

    def missingNumber(self, nums: List[int]) -> int:
        """
        @tags:              位运算
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       使用异或运算 a⊕b⊕b = a   a⊕0=a    a⊕a=0
        """
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i
        for j in nums:
            res ^= j
        return res
