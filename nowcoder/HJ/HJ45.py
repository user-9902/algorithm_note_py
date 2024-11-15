"""
@title:      HJ45 名字的漂亮度
@difficulty: 简单
@importance: 3/5
@tags:       业务题
"""

from collections import Counter

n = int(input())


def res(s):
    res = 0
    cur = 26
    cnt = Counter(s)
    vals = list(cnt.values())
    vals.sort()
    vals.reverse()

    for i in vals:
        res += cur * i
        cur -= 1
    return res


for i in range(n):
    s = input().lower()
    print(res(s))
