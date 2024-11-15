"""
@title:      HJ89 24点运算
@difficulty: 中等
@importance: 4/5
@tags:       fs 业务模拟
@desc:       本题无需考虑运算优先级、无括号、暴力枚举即可
"""

from itertools import permutations

nums_set = ["0", "A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]
str_map = {v: i for i, v in enumerate(nums_set)}
cmd_map = ["+", "-", "*", "/"]


def cal(a, b, cmd):
    if cmd == 0:
        return a + b
    elif cmd == 1:
        return a - b
    elif cmd == 2:
        return a * b
    # 从左向右不会遇到分母为0
    elif cmd == 3:
        return a // b


def cal1(nums):
    # 无运算优先级 fs即可
    for num in permutations(nums):  # 💲全排列组合
        for i in range(4):
            a = cal(num[0], num[1], i)
            for j in range(4):
                b = cal(a, num[2], j)
                for k in range(4):
                    c = cal(b, num[3], k)
                    if c == 24:
                        return "".join(
                            [
                                nums_set[num[0]],
                                cmd_map[i],
                                nums_set[num[1]],
                                cmd_map[j],
                                nums_set[num[2]],
                                cmd_map[k],
                                nums_set[num[3]],
                            ]
                        )


def output(s):
    num = []
    for c in s:
        if c.lower() == "joker":
            return print("ERROR")
        num.append(str_map[c])
    print(cal1(num) or "NONE")


s = input().split()
output(s)
