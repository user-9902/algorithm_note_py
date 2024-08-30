"""
@title:      486. 预测赢家
@difficulty: 中等
@importance: 5/5
@tags:       区间dp 前缀和 博弈
"""

from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        """
        @tags:              区间dp 前缀和              
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       将题目转化为选或不选的问题
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        # 区间dp
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = max(
                    nums[i] + pre[j + 1] - pre[i + 1] - f[i + 1][j],
                    nums[j] + pre[j] - pre[i] - f[i][j - 1],
                )
        return f[0][n - 1] >= pre[n] / 2
