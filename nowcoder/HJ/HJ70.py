"""
@title:      HJ70 矩阵乘法计算量估算
@difficulty: 中等
@importance: 3/5
@tags:       业务模拟
"""

n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]
cmd = input()
stacka = []
stackb = 0  # 左括号个数


def cal(a, b):
    return [a[0], b[1]], a[1] * a[0] * b[1]


ans = 0
for c in cmd:
    if c == "(":
        stackb += 1
    elif c == ")":
        b = stacka.pop()
        a = stacka.pop()
        x, y = cal(a, b)
        ans += y
        stacka.append(x)
        stackb -= 1
    else:
        stacka.append(arr.pop(0))

while len(stacka) > 1:
    a = stacka.pop(0)
    b = stacka.pop(0)
    x, y = cal(a, b)
    ans += y
    stacka = [x] + stacka
print(ans)
