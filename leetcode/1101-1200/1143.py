"""
1143. 最长公共子序列
LCS, dp
最长公共子序列的变形题有很多，是非常经典的区间dp题目
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        区间dp
            f[i][j]表示text1[0-i]、text2[0-j]能组成的最长子序列
            f[i][j] = f[i-1][j-1] + 1 if text1[i] == text2[j] else max(f[i][j-1], f[i-1][j])
        """
        n = len(text1)
        m = len(text2)

        f = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                f[i+1][j+1] = f[i][j] + 1 if text1[i] == text2[j] else max(f[i+1][j], f[i][j+1])
        return f[-1][-1]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """
        dp 空间优化
        分析二维的f，不难发现d依赖a,c,b
        [...a,b...]
        [...c,d...]
        因此还是从前向后遍历。压缩为一维后a可能会被c覆盖，那一个额外变量保存a即可
        """

        n = len(text1)
        m = len(text2)

        f = [0] * (m + 1)

        for i, x in enumerate(text1):
            pre = 0
            for j, y in enumerate(text2):
                tmp = f[j+1]
                f[j+1] = pre + 1 if x == y else max(f[j+1], f[j])
                pre = tmp

        return f[-1]


Solution().longestCommonSubsequence('abcde', 'ace')
