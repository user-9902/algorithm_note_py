"""
216. 组合总和 III
dfs剪枝
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(sum=0, i=1):
            # 剪枝
            if len(cur) == k or sum >= n:
                return

            for j in range(i, 10):
                cur.append(j)
                sum += j

                if sum == n and len(cur) == k:
                    ans.append(cur[:])
                else:
                    dfs(sum, j+1)

                cur.pop()
                sum -= j

        dfs()
        return ans
