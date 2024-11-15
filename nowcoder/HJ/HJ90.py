"""
@title:      HJ90 合法IP
@difficulty: 简单
@importance: 4/5
@tags:       业务模拟
"""

"""
💲
合法 ipv4地址：
    每一位均在 [0,255] 闭区间中

特殊ip：
    全零地址：0.0.0.0   表示“未指定地址”
    广播地址：255.255.255.255   用于本地网络广播
    私有地址：10.0.0.0 - 10.255.255.255
             172.16.0.0 - 172.31.255.255
             192.168.0.0 - 192.168.255.255
    环回地址：127.0.0.0 - 127.255.255.255
    多播地址：224.0.0.0 - 239.255.255.255
    保留地址：240.0.0.0 - 255.255.255.254
"""

s = input()


def isLegal(item):
    if len(item) != 4:
        return False
    for i in item:
        if not str.isdigit(i):
            return False
        if str(int(i)) != i:
            return False
        x = int(i)
        if x > 255:
            return False
    return True


print("YES" if isLegal(s.split(".")) else "NO")
