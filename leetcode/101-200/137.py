"""
137. 只出现一次的数字 II
位运算
参考：https://leetcode.cn/problems/single-number-ii/solutions/2482832/dai-ni-yi-bu-bu-tui-dao-chu-wei-yun-suan-wnwy/?envType=daily-question&envId=2023-10-16
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        模三加法
        对于上一题来说，异或就是将一个数字在 0 -> 1 -> 0 -> 1 之间不断的切换
        这里需要一种在 0 -> 1 -> 2 -> 0 -> 1 -> 2 之间不断切换的过程
        既模三加法  对应的二进制表示为 00 -> 01 -> 10 -> 00 -> 01 -> 10
        """
        a = b = 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b
