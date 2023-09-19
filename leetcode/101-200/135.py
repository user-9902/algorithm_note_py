"""
135. 分发糖果
将问题拆解为 
    rating[i] > rating[i-1] 时需要给出的最少糖果
    rating[i] > rating[i+1] 时需要给出的最少糖果
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [1]
        for i in range(1, n):
            left.append(left[i - 1] + 1 if ratings[i] > ratings[i - 1] else 1)

        res = max(1, left[-1])
        right = 1
        for i in range(n - 2, -1, -1):
            right = right + 1 if ratings[i] > ratings[i+1] else 1
            res += max(right, left[i])

        return res


Solution().candy([1, 3, 5, 2, 3, 4, 3, 3])
