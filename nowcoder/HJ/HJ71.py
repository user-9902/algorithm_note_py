"""
@title:      HJ71 字符串通配符
@difficulty: 中等
@importance: 5/5
@tags:       dp 
@desc:       经典题,见题 leetcode 44
"""

s1 = input()
s2 = input()

n, m = len(s1), len(s2)
f = [[False] * (m + 1) for i in range(n + 1)]
f[0][0] = True

for i in range(n):
    if s1[i] == "*":
        f[i + 1][0] = True
    else:
        break

for i, a in enumerate(s1):
    for j, b in enumerate(s2):
        a = a.lower()
        b = b.lower()
        if a == b and f[i][j]:
            f[i + 1][j + 1] = True
        elif not str.isalnum(b):
            continue
        elif a == "?" and f[i][j]:
            f[i + 1][j + 1] = True
        elif a == "*":
            for k in range(j + 2):
                if f[i][k]:
                    f[i + 1][j + 1] = True
                    break
print(str(f[n][m]).lower())
