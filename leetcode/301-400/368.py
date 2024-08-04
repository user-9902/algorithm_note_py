"""
@title:      368. 最大整除子集
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""

from typing import List
from collections import deque


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        @tags:              sort 序列dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       sort dp即可
        """
        nums.sort()
        n = len(nums)
        f = [[None, 1, nums[i]] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[j][1] + 1 > f[i][1]:
                        f[i][1] = f[j][1] + 1
                        f[i][0] = j
        max_i = max(f, key=lambda x: x[1])
        res = deque()
        while max_i:
            res.appendleft(max_i[2])
            if max_i[0] is None:
                break
            max_i = f[max_i[0]]

        return list(res)
