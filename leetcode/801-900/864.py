"""
@title:      864. 获取所有钥匙的最短路径
@difficulty: 中等
@importance: 5/5
@tags:       dfs
"""

from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        @tags:              dfs
        @time complexity:   O(mn2^k)
        @space complexity:  O(mn2^k)
        @desc:              携带状态信息的dfs。多一维度信息。
        """
        n = len(grid)
        m = len(grid[0])
        u = 0
        queue = []
        for i in range(n):
            for j in range(m):
                if ord('a') <= ord(grid[i][j]) <= ord('z'):
                    u = u | (1 << ord(grid[i][j]) - ord('a'))
                elif grid[i][j] == '@':
                    queue.append([i, j, 0])
        visited = [[[False] * u for _ in range(m)] for i in range(n)]

        res = 0
        while queue:
            xxx = len(queue)
            for _ in range(xxx):
                a, b, v = queue.pop(0)
                if visited[a][b][v]:
                    continue
                visited[a][b][v] = True
                c = grid[a][b]

                if c == '#':
                    # 撞墙
                    continue
                elif ord('A') <= ord(c) <= ord('Z') and (v & (1 << ord(c) - ord('A'))) == 0:
                    # 开不了锁
                    continue
                elif ord('a') <= ord(c) <= ord('z'):
                    # 捡起钥匙
                    v |= (1 << ord(c) - ord('a'))
                    if v == u:
                        return res

                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x += a
                    y += b
                    if x == -1 or x == n or y == -1 or y == m:
                        continue
                    queue.append([x, y, v])
            res += 1
        return -1
