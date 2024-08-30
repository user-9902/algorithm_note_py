"""
@title:      1143. 最长公共子序列
@difficulty: 中等
@importance: 6/5
@tags:       LCS dp
"""

from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        @tags:              递归
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)
        @description:       将问题切割为子问题:
                            f[i][j] = f[i-1][j-1] + 1               text1[i] == text2[j]
                            f[i][j] = max(f[i][j-1], f[i-1][j])     text1[i] != text2[j]         
        """
        n = len(text1)
        m = len(text2)

        @cache
        def dfs(l1, l2):
            # 终止条件
            if l1 == -1 or l2 == -1:
                return 0
            # 两种情况
            elif text1[l1] == text2[l2]:
                return dfs(l1 - 1, l2 - 1) + 1
            else:
                return max(dfs(l1 - 1, l2), dfs(l1, l2 - 1))

        return dfs(n - 1, m - 1)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)  # 分析状态转移方程，能发现，f[i][j] 依赖于他相邻的上、左、左上三个状态。因此可以压缩至一维
        @description:       递归翻译成递推
        """
        n = len(text1)
        m = len(text2)

        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                f[i+1][j+1] = (
                    f[i][j] + 1
                    if text1[i] == text2[j]
                    else max(f[i+1][j], f[i][j+1])
                )
        return f[n][m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        @tags:              dp 状态压缩
        @time complexity:   O(n*m)   
        @space complexity:  O(m)
        @description:       压缩至一维需要注意，状态来自左、上、左上相邻的数据。
                            左上的数据会被左侧的新数据覆盖，需要用一个临时变量单独记录
        """
        n = len(text1)
        m = len(text2)

        f = [0] * (m + 1)

        for i in range(n):
            pre = f[0]
            for j in range(m):
                tmp = f[j+1]
                f[j+1] = (
                    pre + 1
                    if text1[i] == text2[j]
                    else max(f[j+1], f[j])
                )
                pre = tmp
        return f[m]
