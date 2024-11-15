"""
@title:      HJ39 判断两个IP是否属于同一子网
@difficulty: 简单
@importance: /5
@tags:       业务模拟
"""

u = 1 << 7


def valid_mask(ip):
    for i, v in enumerate(ip):
        v = int(v)
        if v and i > 0 and int(ip[i-1]) != 255:
            return False
        while u & v:
            v ^= u
            v <<= 1
        if v:
            return False
    return True


def valid(ip):
    for i in ip:
        if not str.isalnum(i):
            return False
        if not -1 < int(i) < 256:
            return False
    return True


def check(mask, a, b):
    for i in range(4):
        if int(mask[i]) & int(a[i]) != int(mask[i]) & int(b[i]):
            return False
    return True


while True:
    try:
        mask = input().split(".")
        a = input().split(".")
        b = input().split(".")
        if valid_mask(mask) and valid(a) and valid(b):
            print("0" if check(mask, a, b) else "2")
        else:
            print("1")
    except:
        break
