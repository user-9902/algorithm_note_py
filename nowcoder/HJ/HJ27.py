"""
@title:      HJ27 查找兄弟单词
@difficulty: 简单
@importance: 2/5
@tags:       string sort
"""

from collections import Counter
s = input()
s_split = s.split()
n = int(s_split[0])
x = s_split[n+1]
idx = int(s_split[n+2])
cnt = Counter(x)

arr = []
for i in range(1, n+1):
    cur = s_split[i]
    if len(cur) == len(x) and cur != x and Counter(cur) == cnt:
        arr.append(cur)
arr.sort()
print(len(arr))
if idx <= len(arr):
    print(arr[idx - 1])
