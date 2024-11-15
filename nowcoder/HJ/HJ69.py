"""
@title:      HJ69 矩阵乘法
@difficulty: 中等
@importance: 5/5
@tags:       math
"""

x = int(input())
y = int(input())
z = int(input())

a = []
# 矩阵乘法 横*竖
for i in range(x):
    a.append([int(i) for i in input().split()])
b = []
for i in range(y):
    b.append([int(i) for i in input().split()])


def dot(a, b):
    x, y, z = len(a), len(a[0]), len(b[0])
    res = [[0] * z for _ in range(x)]
    for i in range(x):
        for j in range(z):
            for k in range(y):
                res[i][j] += a[i][k] * b[k][j]
    return res


for i in dot(a, b):
    print(" ".join([str(x) for x in i]))
