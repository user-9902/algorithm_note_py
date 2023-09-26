"""
铺地毯
遍历每张地毯，校验的点被覆盖到，覆盖到当前地毯则为最上层地毯
"""
from typing import List


def solution(blanks: List[List[int]], point: List[int]):
    ans = -1
    for i, v in enumerate(blanks):
        if v[0] <= point[0] <= v[0] + v[2] \
                and v[1] <= point[1] <= v[1] + v[3]:
            ans = i + 1
    return ans


if __name__ == '__main__':
    blanks = []
    n = int(input())
    for i in range(n):
        blanks.append(list(map(lambda x: int(x), input().split(' '))))
    point = list(map(lambda x: int(x), input().split(' ')))

    ans = solution(blanks, point)
    print(ans)
