"""
@title:      90. 子集 II
@difficulty: 中等
@importance: 4/5
@tags:       回溯
"""

from functools import cache
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        @tags:              回溯
        @time complexity:   O(n2^n)
        @space complexity:  O(n)
        @description:       去重见  leetcode 40
        """
        n = len(nums)
        nums.sort()
        ans = []
        cur = []

        def dfs(i):
            ans.append(cur.copy())
            if i == n:
                return

            m = {}
            for j in range(i, n):
                if nums[j] in m:
                    continue
                m[nums[j]] = True
                cur.append(nums[j])
                dfs(j + 1)
                cur.pop()

        dfs(0)
        return ans
