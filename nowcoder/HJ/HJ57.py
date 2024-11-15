"""
@title:      HJ57 高精度整数加法
@difficulty: 简单
@importance: 3/5
@tags:       模拟
"""

s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)
n = max(n1, n2)
s1 = s1.rjust(n, "0")
s2 = s2.rjust(n, "0")
premotion = 0
res = ""
for i in range(n - 1, -1, -1):
    a = int(s1[i])
    b = int(s2[i])
    res = str((a + b + premotion) % 10) + res
    premotion = (a + b + premotion) // 10
if premotion:
    res = str(premotion) + res
print(res)
