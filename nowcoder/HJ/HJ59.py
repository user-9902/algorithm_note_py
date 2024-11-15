"""
@title:      HJ59 找出字符串中第一个只出现一次的字符
@difficulty: 简单
@importance: 3/5
@tags:       hashmap
"""

from collections import defaultdict

s = input()
n = len(s)

res = ""
dd = defaultdict(int)
f = [0] * n
for i, c in enumerate(s):
    dd[c] += 1
    f[i] = dd[c]

r = -1
for i in range(n):
    if f[i] == 1 and dd[s[i]] == 1:
        r = s[i]
        break
print(r)
