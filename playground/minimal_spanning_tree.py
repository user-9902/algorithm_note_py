"""
最小生成树
既如何，带权的图中，如何得到一个权值最小的子树
图种连接n个节点最少需要n-1条边，这同时满足了树的定义
参考：https://www.bilibili.com/video/BV1Eb41177d1/?spm_id_from=333.337.search-card.all.click
"""
from math import inf
from typing import List


"""
Kruskal
从边入手
将图中所有的边按照权值从低到高排序
按权值从小到大将边填入图中，若新加入的边使得子树出现回路，则丢弃该条边
直至加入n-1条边时，子树便构建完成
"""


def kruskal(size: int, edges: List[(int)]):
    # 排序
    edges.sort(key=lambda x: x[2])

    for i in edges:
        """
        没实现图的数据结构，这里是实现思路：
            将当前边加入到已经生成的树中
            判断树中是否有环出现：dfs 新加入的点，判断是否回到原点
            无环出现，则是一个有效的边
        """
        pass


"""
Prim
从节点入手
假设从节点A出发
将节点A视为一个整体，剩余所有节点视为一个整体
取连接A和剩余节点的最小权值的边，即可
然后将A和最小权值的边连接的节点视为一个新的整体，再次将剩余节点视为另一个整体即可
"""


def prim(matrix: List[List[int]]) -> list[(int, int, int)]:
    """
    输入邻接矩阵，返回最小生成树子树的边
    """
    n = len(matrix)
    rest = [False] * n
    edges = []

    next = 0
    rest[0] = True
    res = []
    while True:
        for i in range(0, n):
            v = matrix[next][i]
            if v == inf or v == 0 or (rest[next] and rest[i]):
                continue
            else:
                edges.append((next, i, v))

        # 删除非向外连接的点
        for x in range(len(edges) - 1, -1, -1):
            v = edges[x]
            if rest[v[0]] and rest[v[1]]:
                edges.pop(x)

        if len(edges) == 0:
            break

        # 在向外连接的边中挑选权重最小的边
        min_edge = min(edges, key=lambda x: x[2])
        res.append(min_edge)

        if rest[min_edge[0]] == True:
            next = min_edge[1]
        else:
            next = min_edge[0]
        rest[next] = True

    return res


# for test
vexs = [i for i in range(0, 9)]
edgs = [
    (0, 1, 10),
    (0, 5, 11),
    (1, 2, 18),
    (1, 6, 16),
    (1, 8, 12),
    (2, 3, 22),
    (2, 8, 8),
    (3, 4, 20),
    (3, 6, 24),
    (3, 7, 16),
    (3, 8, 21),
    (4, 5, 26),
    (4, 7, 7),
    (5, 6, 17),
    (6, 7, 19),
]


# adjacency matrix
def create_adj_mat(size, edges, direc=False):
    res = [[inf] * size for i in range(size)]
    for i in range(size):
        res[i][i] = 0

    for x, y, w in edges:
        res[x][y] = w
        if not direc:
            res[y][x] = w
    return res


prim(create_adj_mat(9, edgs))

create_adj_mat(9, [(0, 1, 1), (0, 2, 5), (1, 3, 7), (
    1, 4, 5), (1, 2, 3), (2, 4, 1), (2, 5, 7), (3, 4, 2), (3, 6, 3), (4, 5, 3), (4, 6, 6), (4, 7, 9), (5, 7, 5), (6, 7, 2), (6, 8, 7), (7, 8, 4)])
