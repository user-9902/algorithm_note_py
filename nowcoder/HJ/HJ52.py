"""
@title:      HJ52 计算字符串的编辑距离
@difficulty: 中等
@importance: 5/5
@tags:       dp ED 
@desc:       经典题,见题 leetcode 72
"""

s1 = input()
s2 = input()
n, m = len(s1), len(s2)
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    f[i][0] = i
for i in range(m + 1):
    f[0][i] = i

for i, a in enumerate(s1):
    for j, b in enumerate(s2):
        if a == b:
            f[i + 1][j + 1] = f[i][j]
        else:
            # 状态来自上、左、左上 可至一维（左和上代表添加字符、左上代表替换字符
            f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
print(f[n][m])
