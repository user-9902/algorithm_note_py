"""
@title:      1931. 用三种不同颜色为网格涂色
@difficulty: 困难
@importance: 4/5
@tags:       dp 记忆化搜索 3进制
"""
from functools import cache


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        @tags:              dp 记忆化搜索 3进制
        @time complexity:   O(n^2 * 3^2m)
        @space complexity:  O(3^2m)
        @description:       见注释
        """
        # 所有的数的可能 3 进制
        path = []

        def dfs(index: int, pre: int):
            if index == m:
                return path.append(pre)
            for i in range(3):
                if pre % 3 != i:
                    dfs(index + 1, pre * 3 + i)

        for i in range(3):
            dfs(1, i)

        # 所有可能的三进制数种 两数 能否组成相邻行
        length = len(path)
        f = [[False] * length for _ in range(length)]

        def ok(a, b):
            for i in range(m - 1, -1, -1):
                cur = 3**i
                if a // cur == b // cur:
                    return False
                a -= (a // cur) * cur
                b -= (b // cur) * cur
            return True

        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                f[i][j] = ok(path[i], path[j])

        # 结果计算
        @cache
        def dfs2(idx, pre):
            if idx == n:
                return 1
            cur = 0
            for i in range(length):
                if f[pre][i]:
                    cur += 1 * dfs2(idx + 1, i)
            return cur

        return sum(dfs2(1, i) for i in range(length)) % int(1e9 + 7)
