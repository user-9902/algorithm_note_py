"""
name:       79. 单词搜索
difficulty: 中等
importance: 4/5
tags:       dfs 回溯
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        @tags:              回溯
        @time complexity:   O(mn)   
        @space complexity:  O(min(l,mn))
        @description:       dfs
        """
        n, m = len(board), len(board[0])
        k = len(word)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [False] * (n * m)

        def dfs(i, j, idx):
            if idx == k - 1:
                return True
            res = False
            visited[i * m + j] = True
            for a, b in dirs:
                a += i
                b += j
                if (
                    -1 < a < n
                    and -1 < b < m
                    and visited[a * m + b] == False
                    and board[a][b] == word[idx + 1]
                ):
                    res = res or dfs(a, b, idx + 1)
            visited[i * m + j] = False
            return res

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


Solution().exist([["A", "B", "C", "E"], [
    "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
