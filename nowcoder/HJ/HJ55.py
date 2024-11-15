"""
@title:      HJ55 挑7
@difficulty: 简单
@importance: 3/5
@tags:       fs
"""

n = int(input())
res = 0
for i in range(1, n + 1):
    if i % 7 == 0:
        res += 1
        continue
    while i:
        if i % 10 == 7:
            res += 1
            break
        i //= 10
print(res)
