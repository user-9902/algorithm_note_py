"""
@title:      1713. 得到子序列的最少操作次数
@difficulty: 困难
@importance: 5/5
@tags:       dp LIS
"""

from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        @tags:              LCS LIS
        @time complexity:   O(n + mlogm)
        @space complexity:  O(n + m)
        @description:       一眼是LCS的题，但是复杂度会超。
                            本题的所有难点就是在 💲LCS LIS的联系
                            target: 6,4,8,1,3,2      题意target不重复是这里转化能实现的前提
                                    0,1,2,3,4,5

                            arr:    4,7,6,2,3,8,6,1
                                    1, ,0,5,4,2,0,3  将题目转化为在这个数组中寻找最长上升子序列
        """
        m = {v: i for i, v in enumerate(target)}

        stack = []
        for i in arr:
            if i in m:
                val = m[i]
                idx = bisect_left(stack, val)
                if idx == len(stack):
                    stack.append(val)
                else:
                    stack[idx] = val

        return len(target) - len(stack)
