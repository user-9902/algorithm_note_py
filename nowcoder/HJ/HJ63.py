"""
@title:      HJ63 DNA序列
@difficulty: 简单
@importance: 3/5
@tags:       滑动窗口
"""

s = input()
l = int(input())
n = len(s)

cnt = 0
r1 = s[:l]
for i in range(l):
    if s[i] == "C" or s[i] == "G":
        cnt += 1

max_c = cnt
for i in range(l, n):
    if s[i] == "C" or s[i] == "G":
        cnt += 1
    if s[i - l] == "C" or s[i - l] == "G":
        cnt -= 1
    if cnt > max_c:
        r1 = s[i - l + 1: i + 1]
        max_c = cnt
print(r1)
