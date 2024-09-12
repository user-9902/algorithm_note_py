"""
@title:      135. 分发糖果
@difficulty: 中等
@importance: 5/5
@tags:       前缀最值
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        @tags:              前缀最值
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       将问题拆解为 
                            rating[i] > rating[i-1] 时需要给出的最少糖果
                            rating[i] > rating[i+1] 时需要给出的最少糖果
        """
        n = len(ratings)

        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        res = max(1, left[n - 1])
        right = 1
        for i in range(n - 2, -1, -1):
            right = right + 1 if ratings[i] > ratings[i + 1] else 1
            res += max(right, left[i])

        return res
