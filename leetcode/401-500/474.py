"""
@title:      474. 一和零
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""
from typing import List
from functools import cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        @tags:              递推
        @time complexity:   O(nmk)
        @space complexity:  O(nmk)
        @description:       01背包 双容量限制背包
        """
        length = len(strs)
        nums = [[0, 0] for _ in range(length)]
        for i in range(length):
            nums0 = strs[i].count("0")
            nums[i][0] = nums0
            nums[i][1] = len(strs[i]) - nums0

        @cache
        def dfs(i, m1, n1):
            if i < 0:
                return 0
            if m1 < nums[i][0] or n1 < nums[i][1]:
                return dfs(i - 1, m1, n1)
            return max(
                dfs(i - 1, m1, n1),
                dfs(i - 1, m1 - nums[i][0], n1 - nums[i][1]) + 1
            )

        return dfs(length - 1, m, n)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(nmk)
        @space complexity:  O(nmk)  空间复杂度优化同01背包
        @description:       将递推翻译成递归
        """
        length = len(strs)
        nums = [[0, 0] for _ in range(length)]
        for i in range(length):
            nums0 = strs[i].count("0")
            nums[i][0] = nums0
            nums[i][1] = len(strs[i]) - nums0

        f = [[[0] * (n+1) for _ in range(m+1)] for x in range(length+1)]

        for i in range(length):
            for j in range(1, m + 1):
                for k in range(1, n + 1):
                    f[i + 1][j][k] = f[i][j][k]
                    if k >= nums[i][1] and j >= nums[i][0]:
                        f[i + 1][j][k] = max(
                            f[i + 1][j][k],
                            f[i][j - nums[i][0]][k - nums[i][1]] + 1
                        )
        return f[length][m][n]
