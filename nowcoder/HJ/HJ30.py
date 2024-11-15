"""
@title:      HJ29 字符串加解密
@difficulty: 中等
@importance: 3/5
@tags:       业务分析题
"""

s1, s2 = input().split()
n = len(s1) + len(s2)
# 第二步
a1 = []
a2 = []
for i, c in enumerate(s1 + s2):
    if i % 2 == 1:
        a1.append(c)
    else:
        a2.append(c)
a1.sort()
a2.sort()
s = []

idx = 0
for i in range(n):
    s.append(a2[idx])
    a1, a2 = a2, a1
    if len(s) % 2 == 0:
        idx += 1

for i in range(n):
    c = s[i]
    num = -1
    if str.isdigit(c):
        num = int(c)
    elif ord("a") <= ord(c.lower()) <= ord("f"):
        num = ord(c.lower()) - ord("a") + 10
    if num > -1:
        r = 0
        x = 4
        while x:
            r |= num & 1
            r <<= 1
            num >>= 1
            x -= 1
        r >>= 1
        if r > 9:
            r = r - 10 + ord("A")
            r = chr(r)
        else:
            r = str(r)
        s[i] = r
print("".join(s))
