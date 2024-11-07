"""
@title:      516. 最长回文子序列
@difficulty: 中等
@importance: 6/5
@tags:       LPS dp
"""
from functools import cache


class Solution:
    """
    最长回文子序列 可以用最长公共子序列的来解决，正序和逆序的最长公共子序列
    区间dp解中，选或不选的思路也类似最长公共子序列
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        @tags:              递归
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)
        @description:       将问题切割为子问题:
                            f[i][j] = f[i+1][j-1] + 2               s[i] == text2[j]
                            f[i][j] = max(f[i][j-1], f[i+1][j])     s[i] != text2[j]   
        """
        n = len(s)

        @cache
        def dfs(l, r):
            # 边界处理
            if l > r:
                return 0
            elif l == r:
                return 1
            # 两种情况
            elif s[l] == s[r]:
                return dfs(l + 1, r - 1) + 2
            else:
                return max(dfs(l, r - 1), dfs(l + 1, r))

        return dfs(0, n - 1)

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n*m)   
        @space complexity:  O(n*m)  # 可以压缩至一维，观察状态方程，f[i][j] 依赖的是相邻的下、左、左下三个状态
        @description:       递归翻译成递推；注意遍历顺序，这里是从下向上遍历
        """
        n = len(s)

        f = [[0] * n for _ in range(n)]
        # 左侧指针
        for i in range(n - 1, -1, -1):
            # 右侧指针
            f[i][i] = 1
            for j in range(i + 1, n):
                f[i][j] = (
                    f[i + 1][j - 1] + 2
                    if s[i] == s[j]
                    else max(f[i + 1][j], f[i][j - 1])
                )

        return f[0][n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)   
        @space complexity:  O(n) 
        @description:       上一解的空间压缩版本
        """
        n = len(s)

        f = [0] * n

        for i in range(n - 1, -1, -1):
            f[i] = 1
            pre = 0
            for j in range(i + 1, n):
                tmp = f[j]
                if s[i] == s[j]:
                    f[j] = pre + 2
                else:
                    f[j] = max(f[j - 1], f[j])
                pre = tmp
        return f[n - 1]
