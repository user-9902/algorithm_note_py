"""
@title:      851. 喧闹和富有
@difficulty: 中等
@importance: 4/5
@tags:       拓扑排序
"""

from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        m = len(richer)

        # 链式前向星 建图
        heads = [-1] * n
        nxt = [-1] * m
        to = [-1] * m
        # 记录入度
        ind = [0] * n

        for i, (a, b) in enumerate(richer):
            to[i] = b
            nxt[i] = heads[a]
            heads[a] = i
            ind[b] += 1

        f = list(range(n))
        # 拓扑排序
        que = []
        for i in range(n):
            if ind[i] == 0:
                que.append(i)

        while que:
            cur = que.pop(0)
            idx = heads[cur]
            # 遍历 cur 开头的所有边
            while idx != -1:
                toIdx = to[idx]
                if quiet[f[cur]] < quiet[f[toIdx]]:
                    f[toIdx] = f[cur]
                ind[toIdx] -= 1
                if ind[toIdx] == 0:
                    que.append(toIdx)
                idx = nxt[idx]
        return f
