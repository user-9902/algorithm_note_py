"""
过河卒
dp
就是二维的爬楼梯
f[i][j] = f[i-1][j] + f[i][j-1]
"""
from math import inf


def solution(rangex, rangey, breakx, breaky) -> int:
    # 这里可以压缩至一维，但时间复杂度会提升
    f = [[inf] * (rangey+1) for _ in range(rangex+1)]

    point = (
        [breakx, breaky],
        [breakx - 1, breaky - 2],
        [breakx - 1, breaky + 2],
        [breakx + 1, breaky - 2],
        [breakx + 1, breaky + 2],
        [breakx - 2, breaky - 1],
        [breakx - 2, breaky + 1],
        [breakx + 2, breaky - 1],
        [breakx + 2, breaky + 1],
    )

    for a, b in point:
        if a <= rangex and a >= 0 and b <= rangey and b >= 0:
            f[a][b] = 0

    for i in range(0, rangex+1):
        for j in range(0, rangey+1):
            if f[i][j] == 0:
                continue
            if i == 0 and j == 0:
                f[0][0] = 1
            elif i == 0:
                f[0][j] = f[0][j-1]
            elif j == 0:
                f[i][0] = f[i-1][0]
            else:
                f[i][j] = f[i-1][j] + f[i][j - 1]

    return f[-1][-1]


if __name__ == '__main__':
    args = list(map(lambda x: int(x), input().split(' ')))
    ans = solution(*args)
    print(ans)
