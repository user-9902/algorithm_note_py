"""
@title:      HJ44 Sudoku
@difficulty: 中等
@importance: 4/5
@tags:       dfs 回溯 状态压缩
"""

matrix = [[int(i) for i in input().split()] for _ in range(9)]

u = (1 << 9) - 1
row = [u] * 9
col = [u] * 9
mat = [u] * 9

for i in range(9):
    for j in range(9):
        v = matrix[i][j]
        if v == 0:
            continue
        idx = 1 << (v - 1)
        row[i] ^= idx
        col[j] ^= idx
        mat[i // 3 * 3 + j // 3] ^= idx


def check(i, j):
    v = matrix[i][j]
    idx = 1 << (v - 1)
    return row[i] & idx and col[j] & idx and mat[i // 3 * 3 + j // 3] & idx


ans = []


def dfs(i, j):
    if i == 9:
        if not ans:
            for x in range(9):
                ans.append(matrix[x].copy())
        return
    v = matrix[i][j]
    i2, j2 = i + ((j + 1) // 9), (j + 1) % 9
    if v == 0:
        for k in range(9):
            matrix[i][j] = k + 1
            if check(i, j):
                idx = 1 << k

                row[i] ^= idx
                col[j] ^= idx
                mat[i // 3 * 3 + j // 3] ^= idx

                dfs(i2, j2)

                row[i] ^= idx
                col[j] ^= idx
                mat[i // 3 * 3 + j // 3] ^= idx
            matrix[i][j] = 0

    else:
        dfs(i2, j2)


dfs(0, 0)
for i in ans:
    print(" ".join([str(x) for x in i]))
