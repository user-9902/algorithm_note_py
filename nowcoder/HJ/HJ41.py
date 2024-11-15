"""
@title:      HJ41 称砝码
@difficulty: 简单
@importance: 3/5
@tags:       fs
"""

n = int(input())
weight = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
# fs
s = set([0])

for i in range(n):
    for j in range(1, nums[i] + 1):
        for v in list(s):
            s.add(weight[i]+v)

print(len(s))
