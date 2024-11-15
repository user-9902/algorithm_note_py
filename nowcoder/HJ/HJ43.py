"""
@title:      HJ43 迷宫问题
@difficulty: 中等
@importance: 4/5
@tags:       dfs 洪水填充
"""

n, m = [int(i) for i in input().split()]
f = []
for i in range(n):
    f.append([int(i) for i in input().split()])

a = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(i, j):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1 or f[i][j] != 0:
        return False
    f[i][j] -= 1
    if i == n - 1 and j == m - 1:
        f[i][j] -= 1
        return True
    for x, y in a:
        if dfs(x + i, y + j):
            f[i][j] -= 1
            return True
    return False


dfs(0, 0)


def sysout(i, j):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1 or f[i][j] != -2:
        return
    f[i][j] -= 1
    print("({},{})".format(i, j))
    for x, y in a:
        sysout(x + i, y + j)


sysout(0, 0)
