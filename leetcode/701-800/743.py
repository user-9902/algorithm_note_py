"""
@title:      743. 网络延迟时间
@difficulty: 中等
@importance: 5/5
@tags:       dijkstra 链式前向星
"""


from typing import List
from math import inf
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        @tags:              堆优化dijkstra
        @time complexity:   O(mlogn)
        @space complexity:  O(n+m)
        @description:       求最短路径，最短路径中的最大值就是最晚到达的，即结果。
        """
        m = len(times)
        # 建图
        heads = [-1] * (n + 1)
        nxt = [-1] * m
        to = [-1] * m
        val = [-1] * m

        for i, (a, b, v) in enumerate(times):
            to[i] = b
            val[i] = v
            nxt[i] = heads[a]
            heads[a] = i
        # n+1 防溢出
        distance = [inf] * (n + 1)
        visited = [False] * (n + 1)
        hp = []
        # 初始化
        heapq.heappush(hp,  [0, k, k])
        distance[k] = 0

        while hp:
            v, a, b = heapq.heappop(hp)
            if visited[b]:
                continue
            visited[b] = True
            edg = heads[b]
            while True:
                if edg == -1:
                    break
                if visited[to[edg]] == False and (distance[b] + val[edg]) < distance[to[edg]]:
                    distance[to[edg]] = distance[b] + val[edg]
                    heapq.heappush(hp,  [distance[b] + val[edg], b, to[edg]])
                edg = nxt[edg]
        res = max(distance[1:])
        return -1 if res == inf else res
