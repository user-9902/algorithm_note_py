"""
@title:      210. 课程表 II
@difficulty: 简单
@importance: 5/5
@tags:       拓扑排序 Kahn
"""

from typing import List


class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        @tags:              拓扑排序
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       拓扑排序模板题
        """
        # 邻接表
        graph = {i: [] for i in range(n)}
        # 入度
        f = [0] * n
        # 数据录入
        for a, b in prerequisites:
            f[a] += 1
            graph[b].append(a)

        que = []
        for i in range(n):
            # 记录入度为 0 的节点
            if f[i] == 0:
                que.append(i)

        res = []
        while que:
            cur = que.pop(0)
            res.append(cur)
            for i in graph[cur]:
                f[i] -= 1
                # 记录新的入度为 0 的节点
                if f[i] == 0:
                    que.append(i)

        return res if len(res) == n else []


Solution().findOrder(2, [[1, 0]])
