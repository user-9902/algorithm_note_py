"""
@title:      2127. 参加会议的最多员工数
@difficulty: 中等
@importance: 5/5
@tags:       拓扑排序 基环森林
"""

from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
        @tags:              拓扑排序 基环森林
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       拓扑排序 基环森林 分类讨论每个基环树
                            环内点数 == 2 时：
                                可以这样开会： 1 → 2 → 3 ⇄ 4 ← 5 。
                                且多个环内点数为 2 的环不会冲突，即可以一起开会
                            环内点数 > 2 时：
                                只容得下环内的人开会。
                                且不能和别的环一起
        """
        n = len(favorite)
        ind = [0] * n

        for a, b in enumerate(favorite):
            ind[b] += 1

        que = []
        for i in range(n):
            if ind[i] == 0:
                que.append(i)

        f = [1] * n
        while que:
            cur = que.pop(0)
            ind[favorite[cur]] -= 1
            f[favorite[cur]] = max(f[cur] + 1, f[favorite[cur]])
            if ind[favorite[cur]] == 0:
                que.append(favorite[cur])

        # 环 == 2 总计
        ans1 = 0
        # 环 > 2 最大
        ans2 = 0
        # 基环森林
        for i in range(n):
            if ind[i] == 1:
                j = i
                cnt = 0
                res = 0
                # 处理每个环
                while ind[j] == 1:
                    cnt += 1
                    res += f[j]
                    ind[j] = 0
                    j = favorite[j]
                if cnt == 2:
                    ans1 += res
                else:
                    ans2 = max(ans2, cnt)
        return max(ans1, ans2)
