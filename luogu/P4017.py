"""
@title:      P4017 最大食物链计数
@difficulty: 中等
@importance: 5/5
@tags:       链式前向星 拓扑排序 dp
"""

string = input().split(" ")
n = int(string[0])
m = int(string[1])

# 链式前向星 ❌ 已优化至链式前向星，但空间复杂度还是超了，py无法 AC
heads = [-1] * (n + 1)
nxt = [-1] * m
to = [-1] * m

# 入度数量记录
inner = [0] * (n + 1)
for i in range(m):
    string1 = input().split(" ")
    a = int(string1[0])
    b = int(string1[1])

    to[i] = b
    inner[b] += 1
    nxt[i] = heads[a]
    heads[a] = i

f = [0] * (n + 1)
que = []
for i in range(1, n+1):
    if inner[i] == 0:
        que.append(i)
        f[i] = 1

while que:
    cur = que.pop(0)
    # 第一条边的下标
    idx = heads[cur]
    while idx != -1:
        # 减少入度
        inner[to[idx]] -= 1
        if inner[to[idx]] == 0:
            que.append(to[idx])
        # 路径数量计算
        f[to[idx]] += f[cur]
        # 下一条边长
        idx = nxt[idx]

res = sum((f[i] if heads[i] == -1 else 0) for i in range(1, n+1))
print(res)
