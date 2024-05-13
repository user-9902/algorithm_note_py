"""
260. 只出现一次的数字 III
位运算，集合

参考：https://leetcode.cn/problems/single-number-iii/solutions/2484352/tu-jie-yi-zhang-tu-miao-dong-zhuan-huan-np9d2/?envType=daily-question&envId=2023-10-16
"""
from typing import List
from operator import xor
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        异或
        两个数是不同的，两个目标数的异或结果中，值为1的比特位，即可区分这两个数。 
            如 0101 ^ 1111 = 1010 那么 0010或1000 即使区分这两个数
        获取一个比特位，进行分组再次异或
        """
        xor_all = reduce(xor, nums)
        bit = xor_all & -xor_all

        ans = [0, 0]
        for n in nums:
            ans[(n & bit) == 0] ^= n
        return ans
