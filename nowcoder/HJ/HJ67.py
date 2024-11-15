"""
@title:      HJ67 24点游戏算法
@difficulty: 中等
@importance: 5/5
@tags:       回溯
@desc:       同 leetcode 679
"""


def dfs(arr):
    n = len(arr)
    if n == 0:
        return False
    if n == 1:
        # 考虑浮点精度
        return abs(arr[0] - 24) < 1e-6
    # 任意选两个不同的数
    for i, a in enumerate(arr):
        for j, b in enumerate(arr):
            if i == j:
                continue
            # 下一轮
            arr2 = []
            for k, x in enumerate(arr):
                if k != i and k != j:
                    arr2.append(x)
            # 遍历所有的 a b 的运算结果
            for cmd in range(4):
                if cmd == 0:
                    arr2.append(a + b)
                elif cmd == 1:
                    arr2.append(a - b)
                elif cmd == 2:
                    arr2.append(a * b)
                elif cmd == 3:
                    # 分母不为 0
                    if abs(b) < 1e-6:
                        continue
                    arr2.append(a / b)
                if dfs(arr2):
                    return True
                arr2.pop()
    return False


arr = [int(i) for i in input().split()]
print(str(dfs(arr)).lower())
