"""
516. 最长回文子序列

"""
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dfs
        """
        n = len(s)

        @cache
        def dfs(i: int, j: int):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i+1, j-1) + 2
            return max(dfs(i+1, j), dfs(i, j-1))

        return dfs(0, n-1)

    def longestPalindromeSubseq2(self, s: str) -> int:
        """
        dp
        dp[i][j] 表示i-j之间的最长回文串
        s[i] == s[j]   dp[i][j] = dp[i + 1][j - 1] + 2
        else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        """
        n = len(s)
        f = [[0]*n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])

        return f[0][n-1]
