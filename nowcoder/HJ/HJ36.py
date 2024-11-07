"""
@title:      HJ36 字符串加密
@difficulty: 简单
@importance: 3/5
@tags:       业务题 二进制优化
"""

key = input()
string = input()
u = (1 << 26) - 1
mp = []
for c in key:
    idx = ord(c) - ord('a')
    if u & (1 << idx):
        mp.append(c)
        u ^= (1 << idx)
idx = 0
while u:
    if u & 1:
        mp.append(chr(ord('a')+idx))
    idx += 1
    u >>= 1
print(mp)
res = ''
for c in string:
    idx = ord(c) - ord('a')
    res += mp[idx]
print(res)
