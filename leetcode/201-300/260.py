"""
@title:      260. 只出现一次的数字 III
@difficulty: 中等
@importance: 5/5
@tags:       hashmap 异或和
"""


from typing import List
from operator import xor
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       统计元素出现次数
        """
        pass

    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        @tags:              异或和
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       前置题 leetcode 136
                            设结果为 a 和 b 我们对nums中的所有元素做异或和结果为 a^b
                            为了将 a 和 b 区分开来，我们需要找到二进制 a 和 b 中不同的那一位
                            💲由于补码的性质 x & -x == x 中最小的一位 1。（如 10101 & 01011 == 00001
                            我们就用这一位数来区分 a 和 b 
        """
        xor_all = reduce(xor, nums)
        bit = xor_all & -xor_all

        # 确保了 a 和 b 在不同的两组中后 将 nums 分为两组，两组内的数分别求异或和
        ans = [0, 0]
        for n in nums:
            ans[(n & bit) == 0] ^= n
        return ans
