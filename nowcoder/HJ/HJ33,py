"""
@title:      HJ33 整数与IP地址间的转换
@difficulty: 简单
@importance: 3/5
@tags:       业务题
"""

s1 = input()
s2 = input()


def encode(s):
    res = 0
    for i in s.split('.'):
        res <<= 8
        res += int(i)
    return res


def decode(s):
    num = int(s)
    ans = []
    for _ in range(4):
        ans.append(num & ((1 << 8) - 1))
        num >>= 8
    ans.reverse()
    return '.'.join([str(i) for i in ans])


print(encode(s1))
print(decode(s2))
