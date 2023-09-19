"""
最短路径
"""
from math import inf
from typing import List


def dijkstra(matrix: List[List[int]], start: int, end: int) -> int:
    """
    greedy
    从根节点出发，维护最短路径列表
    从最短路径列表中挑选出最短的路径，选出下一个节点
    """
    n = len(matrix)
    # 到达对应节点的最短距离，前一个节点
    res = [[inf, None] for _ in range(n)]
    fin = [False] * n

    res[start][0] = 0
    res[start][1] = start
    fin[start] = True

    cur = start
    while True:
        # 更新 res
        for i, v in enumerate(matrix[cur]):
            if v == inf or v == 0 or fin[i]:
                continue
            res[i][0] = min(res[i][0], v + res[cur][0])
            res[i][1] = cur
        # 找寻res中的最小路径
        min_i = None
        for x, y in enumerate(res):
            if fin[x] or y[0] == inf:
                continue
            if min_i is None or res[min_i][0] > y[0]:
                min_i = x
        # 下一轮的工作
        if min_i == None:
            break
        fin[min_i] = True
        cur = min_i
        # 得到end的最短即可停止
        if min_i == end:
            break

    return res[end][0]


def floyd(matrix: List[List[int]]):
    """
    dp
    依次以每个节点为中转节点，遍历每个节点，搜寻更短的路径
    """
    n = len(matrix)

    d = matrix.copy()
    p = [[i for i in range(n)] for _ in range(n)]

    # 依次把每个节点作为中间节点
    for i in range(n):
        # 遍历每个节点，搜寻是否存在更优路径
        for x in range(n):
            if x == i:
                continue
            for y in range(n):
                if y == i or x == y:
                    continue
                if d[x][y] > d[x][i] + d[i][y]:
                    d[x][y] = d[x][i] + d[i][y]
                    p[x][y] = i
    return (d, p)


def bellman_ford():
    pass


test_matrix = [
    [0, 1, 5, inf, inf, inf, inf, inf, inf],
    [1, 0, 3, 7, 5, inf, inf, inf, inf],
    [5, 3, 0, inf, 1, 7, inf, inf, inf],
    [inf, 7, inf, 0, 2, inf, 3, inf, inf],
    [inf, 5, 1, 2, 0, 3, 6, 9, inf],
    [inf, inf, 7, inf, 3, 0, inf, 5, inf],
    [inf, inf, inf, 3, 6, inf, 0, 2, 7],
    [inf, inf, inf, inf, 9, 5, 2, 0, 4],
    [inf, inf, inf, inf, inf, inf, 7, 4, 0]
]

dijkstra(test_matrix, 0, 8)
floyd(test_matrix)
