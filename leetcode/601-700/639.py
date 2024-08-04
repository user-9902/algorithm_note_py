"""
@title:      639. 解码方法 II
@difficulty: 中等
@importance: 5/5
@tags:       线性dp
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(n)    
        @description:       较前置题(leetcode 91)思路是一致的，但多了许多分类情况的讨论
        """
        MOD = 10**9 + 7

        n = len(s)
        f = [0] * n
        f[0] = 0 if s[0] == "0" else 1

        for i in range(n):
            # 一个字符
            if i == 0:
                f[i] = 9 if s[i] == "*" else 0 if s[i] == "0" else 1
            else:
                f[i] = 9 * f[i - 1] if s[i] == "*" else 0 if s[i] == "0" else f[i - 1]
            # 两个字符
            if i > 0:
                if s[i] != "*":
                    if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6"):
                        f[i] += f[i - 2] if i > 1 else 1
                    if s[i - 1] == "*":
                        if s[i] <= "6":
                            f[i] += f[i - 2] * 2 if i > 1 else 2
                        else:
                            f[i] += f[i - 2] * 1 if i > 1 else 1
                else:
                    if s[i - 1] == "*":
                        f[i] += f[i - 2] * 15 if i > 1 else 15
                    elif s[i - 1] == "1":
                        f[i] += f[i - 2] * 9 if i > 1 else 9
                    elif s[i - 1] == "2":
                        f[i] += f[i - 2] * 6 if i > 1 else 6
            f[i] %= MOD
        return f[n - 1]
