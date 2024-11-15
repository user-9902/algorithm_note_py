"""
@title:      HJ88 扑克牌大小
@difficulty: 简单
@importance: 3/5
@tags:       业务模拟
"""

num_list = [str(i) for i in range(3, 11)] + \
    ["J", "Q", "K", "A", "2", "joker", "JOKER"]
num_mp = {v: i for i, v in enumerate(num_list)}

a, b = input().split("-")


def compare(a, b):
    # 王炸
    if a == "joker JOKER" or b == "joker JOKER":
        return "joker JOKER"

    arra = a.split()
    arrb = b.split()

    # 炸弹
    flag = False
    r = "3"
    if len(arra) == 4 and num_mp[arra[0]] > num_mp[r[0]]:
        flag = True
        r = arra[0]
    if len(arrb) == 4 and num_mp[arrb[0]] > num_mp[r[0]]:
        flag = True
        r = arrb[0]
    if flag:
        return ' '.join([r] * 4)

    if len(arra) != len(arrb):
        return "ERROR"

    if num_mp[arra[0]] > num_mp[arrb[0]]:
        return a
    else:
        return b


print(compare(a, b))
