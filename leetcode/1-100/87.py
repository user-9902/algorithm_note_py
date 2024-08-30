"""
@title:      87. 扰乱字符串
@difficulty: 中等
@importance: 5/5
@tags:       记忆化搜索 dp
"""
from collections import Counter
from functools import cache


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        @tags:              记忆化搜索
        @time complexity:   O(n^4)   
        @space complexity:  O(n^3)
        @description:       将问题切割为子问题即可。本题的记忆化搜索解更简单，且方便理解
        """
        n, m = len(s1), len(s2)

        # 边界条件
        if n != m:
            return False
        if Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True

        # 切割 重新判断
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        @tags:              区间dp
        @time complexity:   O(n^3)   
        @space complexity:  O(n^3)
        @description:       将上述问题转化为dp
        """

        n = len(s1)
        if n != len(s2):
            return False

        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])

        # 枚举长度
        for length in range(2, n + 1):
            # 枚举s1起点
            for i in range(n - length + 1):
                # 枚举s2起点
                for j in range(n - length + 1):
                    # 枚举切割点
                    for k in range(1, length):
                        if (dp[i][j][k] and dp[i+k][j+k][length-k]):
                            return True
                        if (dp[i][j + length - k][k] and dp[i + k][j][length - k]):
                            return True
        return False
