"""
@title:      HJ16 购物单
@difficulty: 中等
@importance: 5/5
@tags:       分组背包
"""

# 数据录入
cap, n = [int(i) for i in input().split()]
cap //= 10
groups = {}
childs = {}
for i in range(n):
    weight, value, idx = [int(x) for x in input().split()]
    weight //= 10
    if idx == 0:
        groups[i + 1] = [weight, value * weight]
    else:
        if idx not in childs:
            childs[idx] = []
        childs[idx].append([weight, value * weight])
# 分组
arr = []
for i in groups.keys():
    cur = []
    cur.append(groups[i])
    arr.append(cur)
    if i in childs:
        for x, y in childs[i]:
            cur.append([groups[i][0] + x, groups[i][1] + y])

        if len(childs[i]) == 2:
            cur.append(
                [
                    groups[i][0] + childs[i][0][0] + childs[i][1][0],
                    groups[i][1] + childs[i][0][1] + childs[i][1][1],
                ]
            )
# 分组背包
group_num = len(arr)
f = [0] * (cap + 1)
for i in range(1, group_num + 1):
    for j in range(cap, -1, -1):
        for weight, value in arr[i - 1]:
            if j >= weight:
                f[j] = max(f[j], f[j - weight] + value)
print(f[cap] * 10)
