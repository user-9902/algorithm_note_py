"""
@title:      115. 不同的子序列 I
@difficulty: 中等
@importance: 5/5
@tags:       线性dp
"""

from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        @tags:              全排列组合
        @time complexity:   O(n^2)
        @space complexity:  O(2^n)  ❌ 栈溢出，需转为dp
        """
        MOD = 10**9 + 7
        n, m = len(s), len(t)

        @cache
        def dfs(i, pre):
            l = len(pre)

            if l == m:
                return 1 if t == pre else 0
            if i == n:
                return 0

            return dfs(i + 1, pre + s[i]) + dfs(i + 1, pre)

        return dfs(0, "") % MOD

    def numDistinct(self, s: str, t: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(mn)   观察状态方程 复杂度可压缩至一维
        """
        MOD = 10**9 + 7
        n, m = len(s), len(t)

        f = [[0] * (m + 1) for _ in range(n + 1)]
        # 两个空串匹配
        f[0][0] = 1

        for i in range(1, n + 1):
            f[i][0] = 1
            for j in range(1, m + 1):
                # t 的增加不影响结果
                f[i][j] = f[i - 1][j]
                # 最后字符串相同的时候
                if s[i - 1] == t[j - 1]:
                    f[i][j] += f[i - 1][j - 1]
                f[i][j] %= MOD

        return f[n][m]
