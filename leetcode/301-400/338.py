"""
@title:      338. 比特位计数
@difficulty: 中等
@importance: 4/5
@tags:       位运算 dp
"""

from typing import List


class Solution:
    """
    0 0 0   0
    0 0 1   1
    0 1 0   2
    0 1 1   3
    1 0 0   4
    1 0 1   5
    1 1 0   6
    1 1 1   7
    """

    def countBits(self, n: int) -> List[int]:
        """
        @tags:              位运算
        @time complexity:   O(nlogn)   
        @space complexity:  O(1)
        @description:       计算每个数字中1的个数
        """
        res = [0] * (n + 1)
        for i in range(n + 1):
            cur = 0
            num = i
            while num:
                cur += 1 if num % 2 else 0
                num >>= 1
            res[i] = cur
        return res

    def countBits(self, n: int) -> List[int]:
        """
        @tags:              dp 位运算
        @time complexity:   O(n)   
        @space complexity:  O(n1)
        @description:       查找去除最高位的1的个数
        """
        if n == 0:
            return [0]
        res = [0] * (n + 1)
        res[1] = 1

        highBit = 0
        for i in range(2, n + 1):
            # 去掉最高位 在表中就能查到去除最高位后1的数量
            if i & (i - 1) == 0:    # 💲存在进位的技巧
                highBit = i
            res[i] = res[i - highBit] + 1

        return res
