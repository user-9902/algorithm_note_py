"""
@title:      827. 最大人工岛
@difficulty: 中等
@importance: 4/5
@tags:       dfs bfs
"""
from typing import List

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        @tags:              洪水填充
        @time complexity:   O(nm)
        @space complexity:  O(1)
        @description:       解题思路即洪水填充，代码的实现有不少细节。
        """
        n = len(grid)

        arr = []

        def dfs(i, j):
            size = 1
            grid[i][j] = len(arr) + 2
            for a, b in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                if 0 <= a <= n-1 and 0 <= b <= n-1 and grid[a][b] == 1:
                    size += dfs(a, b)
            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    arr.append(dfs(i, j))

        if len(arr) == 0:
            return 1

        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                s = set()
                for a, b in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= a <= n-1 and 0 <= b <= n-1 and grid[a][b]:
                        s.add(grid[a][b])
                res = max(res, sum(arr[i-2] for i in s) + 1)

        return n*n if res == 0 else res
