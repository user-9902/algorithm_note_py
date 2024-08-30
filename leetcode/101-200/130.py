"""
@title:      130. 被围绕的区域
@difficulty: 简单
@importance: 5/5
@tags:       dfs bfs
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        @tags:              洪水填充
        @time complexity:   O(nm)
        @space complexity:  O(1)
        @description:       dfs bfs 遍历都可以，重点是在填充（标记）上。
                            常有类似的题会以水为背景，有着类似的解题思路。
        """
        n, m = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i <= n - 1 and 0 <= j <= m - 1:
                if board[i][j] == "O":
                    board[i][j] = "T"
                    dfs(i + 1, j)
                    dfs(i - 1, j)
                    dfs(i, j + 1)
                    dfs(i, j - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
