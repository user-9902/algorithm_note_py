"""
@title:      2710. 移除字符串中的尾随零
@difficulty: 简单
@importance: 1/5
@tags:       string
"""
from typing import List


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        """
        @tags:              binary_search sort
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       遍历即可
        """
        n = len(num)
        res = 0
        for i in range(n-1, -1, -1):
            if num[i] != '0':
                break
            else:
                res -= 1
        return num if res == 0 else num[:res]

    def removeTrailingZeros(self, num: str) -> str:
        """
        @description:       熟悉下api
        """
        return num.rstrip('0')
