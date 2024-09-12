"""
@title:      136. 只出现一次的数字
@difficulty: 简单
@importance: 5/5
@tags:       异或和
"""
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        @tags:              模2运算
        @time complexity:   O(32n)
        @space complexity:  O(n)
        @description:        110
                            +110
                            +011
                            =231
                按位模2不进位=011
        """
        mod = 2
        f = [0] * 32
        minuse = 0
        for num in nums:
            if num < 0:
                num = -num
                minuse += 1
            i = 0
            while num:
                if num & 1:
                    f[i] += 1
                num >>= 1
                i += 1
        res = 0
        for i, v in enumerate(f):
            res += (v % mod) * 2**i
        return -res if minuse % mod else res

    def singleNumber(self, nums: List[int]) -> int:
        """
        @tags:              异或和
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       💲异或和的一些特性
                            a ^ a = 0
                            a ^ 0 = 1
                            a ^ 1 = ~a
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans

        # return reduce(xor, nums)  # 一行
