"""
@title:      39. 组合总和
@difficulty: 简单
@importance: 4/5
@tags:       回溯
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        @tags:              回溯
        @time complexity:   O(n^target)
        @space complexity:  O(n*target)
        @description:       枚举的所以可能
        """
        n = len(candidates)
        ans = []
        path = []

        def dfs(idx, t):
            if t <= 0:
                if t == 0:
                    ans.append(path[::])
                return

            for i in range(idx, n):
                path.append(candidates[i])
                dfs(i, t - candidates[i])
                path.pop()

        dfs(0, target)
        return ans
