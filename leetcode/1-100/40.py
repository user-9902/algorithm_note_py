"""
@title:      40. 组合总和 II
@difficulty: 中等
@importance: 5/5
@tags:       回溯 剪枝
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        @tags:              回溯 剪枝
        @time complexity:   O(n^target)
        @space complexity:  O(n*target)
        @description:       如何去重？用 1 2 2 2 5 举例，将dfs遍历的过程转化为树结构，去重就是避免重复的路径。如 1->2->... 的路径多次出现。
                            root
                1                   2               2       2       5
            2   2   2   5       1   2   2   5    .......
        """
        n = len(candidates)
        candidates.sort()

        ans = []
        cur = []

        def dfs(i, t):
            if t <= 0:
                if t == 0:
                    ans.append(cur.copy())
                return
            if i == n:
                return
            m = {}
            for j in range(i, n):
                # 剪枝 去重
                if candidates[j] in m and m[candidates[j]]:
                    continue
                m[candidates[j]] = True
                cur.append(candidates[j])
                dfs(j + 1, t - candidates[j])
                cur.pop()
        dfs(0, target)
        return ans


Solution().combinationSum2([2, 5, 2, 1, 2], 5)
