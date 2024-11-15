"""
@title:      HJ82 将真分数分解为埃及分数
@difficulty: 中等
@importance: 5/5
@tags:       贪心 math
@desc:       a/b <= 1/x
             b/a <= x
             需要寻找满足条件的最小正整数x
             x = math.ceil(b / a) 向上取整
"""


def cal(a, b):
    fractions = []

    while a > 0:
        # 找到最小的 x 使得 1/x <= a/b
        # 等价于 math.ceil(b / a)
        x = (b + a - 1) // a

        # 添加 1/x 到结果列表
        fractions.append(x)

        # 更新 a 和 b
        a = a * x - b
        b = b * x

    return fractions


while True:
    try:
        a, b = [int(i) for i in input().split('/')]
        ans = cal(a, b)
        print("+".join(["1/{}".format(i) for i in ans]))
    except:
        break
