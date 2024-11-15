"""
@title:      J103 Redraiment的走法
@difficulty: 简单
@importance: 5/5
@tags:       LIS
@desc:       最长递增子序列 经典题
"""


n = int(input())
arr = [int(i) for i in input().split()]
f = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            f[i] = max(f[i], f[j] + 1)
print(max(f))
