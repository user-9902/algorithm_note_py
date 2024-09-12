"""
@title:      137. 只出现一次的数字 II
@difficulty: 中等
@importance: 5/5
@tags:       模3运算 
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        @tags:              模3运算
        @time complexity:   O(32n)
        @space complexity:  O(n)
        @description:        110    同 leetcode 136
                            +110
                            +110
                            +011
                            =341
                按位模3不进位=011
        """
        mod = 3
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
        @tags:              电路设计
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       需要一种设计一种结构，使得状态在 00 -> 01 -> 10 -> 00 -> 01 -> ...之间切换
                            见：https://leetcode.cn/problems/single-number-ii/solutions/8944/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
        """
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
