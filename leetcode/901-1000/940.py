"""
@title:      940. 不同的子序列 II
@difficulty: 中等
@importance: 5/5
@tags:       线性dp
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n*c^2)
        @space complexity:  O(n*c)
        @description:       本题乍一看是01背包问题，但是不能去除重复的序列，见注释。
        """
        MOD = 10 ** 9 + 7
        n,  = len(s)

        f = [[0] * 26 for _ in range(n + 1)]

        for i in range(1, n + 1):
            c = ord(s[i - 1]) - ord("a")
            for j in range(26):
                # f[i][j] 表示前i个字符以j结尾有多少种组合
                # 不以 s[i] 结尾  or  以 s[i] 结尾
                f[i][j] = f[i - 1][j] if c != j else (1 + sum(f[i - 1])) % MOD

        return sum(f[n]) % MOD

    def distinctSubseqII(self, s: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(c)
        @description:       上面算法的空间优化 + 时间优化
        """
        MOD = 10**9 + 7
        n = len(s)
        f = [0] * 26
        total = 0
        for i in range(n):
            idx = ord(s[i]) - ord("a")
            prev = f[idx]
            f[idx] = (total + 1) % MOD
            total = (total + f[idx] - prev) % MOD

        return sum(f) % MOD
