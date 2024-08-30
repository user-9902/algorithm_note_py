"""
@title:      78. 子集
@difficulty: 简单
@importance: 4/5
@tags:       回溯
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        @tags:              回溯
        @time complexity:   O(n2^n)
        @space complexity:  O(n)
        @description:       选或不选
        """
        n = len(nums)
        ans = []
        cur = []

        def dfs(i):
            if i == n:
                ans.append(cur.copy())
                return
            # 不选
            dfs(i + 1)
            # 选
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()  # 恢复现场

        dfs(0)
        return ans
