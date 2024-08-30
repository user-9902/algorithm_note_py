"""
@title:      并查集
@difficulty: 困难
@importance: 4/5
@tags:       并查集
"""

"""
我们有集合 {1} {2} {3} {4} {5} {6} 下面我们会对集合进行合并操作,判断两元素是否在同一集合.
"""


class UnionFind:
    def __init__(self, size):
        # 初始化并查集，size 表示并查集中元素的数量
        self.heads = list(range(size))
        self.stack = [0] * size  # 用于优化合并操作

    def find(self, x):
        # 查找元素 x 所属的集合的根节点
        if self.heads[x] != x:
            # 路径压缩
            self.heads[x] = self.find(self.heads[x])
        return self.heads[x]

    def union(self, x, y):
        # 合并元素 x 和 y 所属的集合
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.stack[rootX] > self.stack[rootY]:
                self.heads[rootY] = rootX
            elif self.stack[rootX] < self.stack[rootY]:
                self.heads[rootX] = rootY
            else:
                self.heads[rootY] = rootX
                self.stack[rootX] += 1

    def connected(self, x, y):
        # 判断元素 x 和 y 是否属于同一个集合
        return self.find(x) == self.find(y)
