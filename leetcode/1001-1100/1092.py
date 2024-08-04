"""
@title:      1092. 最短公共超序列
@difficulty: 中等
@importance: 4/5
@tags:       dp LCS
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        @tags:              dp
        @time complexity:   O(nm)
        @space complexity:  O(m)
        @description:       LCS 最长公共子序列 然后构造结果串
        """
        n, m = len(str1), len(str2)
        f = [""] * (m + 1)
        for i in range(n):
            pre = ""
            for j in range(m):
                tmp = f[j + 1]
                if str1[i] == str2[j]:
                    f[j + 1] = pre + str1[i]
                else:
                    f[j + 1] = f[j + 1] if len(f[j + 1]) > len(f[j]) else f[j]
                pre = tmp

        res = f[m]

        a = b = c = 0
        # 补齐非公共子序列的部分
        while c < len(res):
            while str1[a] != res[c]:
                res = res[:c] + str1[a] + res[c:]
                a += 1
                c += 1
            while str2[b] != res[c]:
                res = res[:c] + str2[b] + res[c:]
                b += 1
                c += 1
            a += 1
            b += 1
            c += 1
        return res + str1[a:] + str2[b:]
