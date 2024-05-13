"""
136. 只出现一次的数字
位运算
"""
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        异或
        a ^ a = 0
        a ^ 0 = 1
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans

    def singleNumber(self, nums: List[int]) -> int:
        """
        异或
        a ^ a = 0
        a ^ 0 = 1
        """
        return reduce(xor, nums)
