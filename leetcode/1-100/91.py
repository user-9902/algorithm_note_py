"""
91. 解码方法
dp
分析好 dp[i - 1] 和 dp[i - 2] 即可
leetcode 官方的题解十分的巧妙
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * n

        for i in range(n):
            # 首位字符处理
            if i == 0:
                if s[1] != 0:
                    f[i] = 1
            else:
                # f[i - 1]
                # 当前字符不为零一定能作为独立字符跟在f[i-1]后面
                if s[i] != '0':
                    f[i] = f[i - 1]
                # f[i - 2]
                # 当前字符 == 0 时只能跟在字符 1 或 2后面
                # 当前字符 != 0 时看是否能和前一个字符组成新的字符
                if s[i - 1] == '1' or s[i - 1] == '2':
                    v = int(s[i-1:i+1])
                    if v < 27:
                        f[i] += 1 if i == 1 else f[i-2]
        return f[-1]
