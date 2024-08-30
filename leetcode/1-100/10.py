"""
@title:      10. 正则表达式匹配
@difficulty: 困难
@importance: 4/5
@tags:       dp
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        @tags:              dp
        @time complexity:   O(mn)
        @space complexity:  O(mn)
        @description:       分类讨论
        """
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True

        for i in range(m):
            if p[i] == "*" and f[0][i - 1]:
                f[0][i + 1] = True

        for i in range(n):
            for j in range(m):
                if p[j] == "*":
                    if f[i + 1][j - 1]:  # 作为空串
                        f[i + 1][j + 1] = True
                    elif s[i] == p[j - 1] and f[i][j + 1]:  # 作为多个前缀字符
                        f[i + 1][j + 1] = True
                    elif p[j - 1] == "." and f[i][j + 1]:  # 作为多个.
                        f[i + 1][j + 1] = True
                elif p[j] == ".":
                    if f[i][j]:
                        f[i + 1][j + 1] = True
                else:
                    if f[i][j] and s[i] == p[j]:
                        f[i + 1][j + 1] = True
        return f[n][m]
