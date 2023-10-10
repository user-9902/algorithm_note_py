"""
39. 组合总和
dfs; 回溯
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        cur = []

        def dfs(rest, index=0):
            for i in range(index, n):
                if rest == 0:
                    ans.append(cur[:])
                    return
                if candidates[i] > rest:
                    continue
                else:
                    cur.append(candidates[i])
                    dfs(rest-candidates[i], i)
                    cur.pop()
        dfs(target)

        return ans
