"""
@title:      2050. 并行课程 III
@difficulty: 中等
@importance: 5/5
@tags:       拓扑排序 dp
"""

from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        @tags:              拓扑排序 dp
        @time complexity:   O(m+n)
        @space complexity:  O(m+n)
        @description:       拓扑排序模板
        """
        m = len(relations)
        heads = [-1] * (n + 1)
        nxt = [-1] * m
        to = [-1] * m
        ind = [0] * (n + 1)
        # 录入信息
        for i, (a, b) in enumerate(relations):
            to[i] = b
            nxt[i] = heads[a]
            heads[a] = i
            ind[b] += 1
        que = []

        f = [0] + time.copy()
        for i in range(1, n + 1):
            if ind[i] == 0:
                que.append(i)

        while que:
            cur = que.pop(0)
            idx = heads[cur]
            while idx != -1:
                toIdx = to[idx]
                f[toIdx] = max(f[toIdx], f[cur] + time[toIdx - 1])

                ind[toIdx] -= 1
                if ind[toIdx] == 0:
                    que.append(toIdx)
                idx = nxt[idx]

        return max(f)
