"""
@title:      HJ65 查找两个字符串a,b中的最长公共子串
@difficulty: 中等
@importance: 5/5
@tags:       dp LCS
"""

s1 = input()
s2 = input()
if len(s1) > len(s2):
    s1, s2 = s2, s1
n, m = len(s1), len(s2)
f = [[0] * (m + 1) for _ in range(n + 1)]

res = ""
for i in range(n):
    for j in range(m):
        # 类lcs
        if s1[i] == s2[j]:
            f[i + 1][j + 1] = f[i][j] + 1
            if f[i + 1][j + 1] > len(res):
                res = s1[i - f[i + 1][j + 1] + 1: i + 1]
print(res)
