"""
@title:      HJ92 在字符串中找出连续最长的数字串
@difficulty: 简单
@importance: 3/5
@tags:       业务模拟
"""


def output(s):
    n = len(s)
    f = [0] * (n + 1)
    for i, c in enumerate(s):
        if str.isdigit(c):
            f[i + 1] = f[i] + 1
    max_v = max(f)
    res = ""
    for i in range(1, n + 1):
        if f[i] == max_v:
            res += s[i - max_v: i]
    return res + "," + str(max_v)


while True:
    try:
        print(output(input()))
    except:
        break
