"""
@title:      807. 保持城市天际线
@difficulty: 简单
@importance: 3/5
@tags:       greedy
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        @tags:              greedy
        @time complexity:   O(m*n)
        @space complexity:  O(m+n)
        @description:       
        """
        n = len(grid)
        row = [0] * n
        col = [0] * n
        for i in range(n):
            for j in range(n):
                row[j] = max(row[j], grid[i][j])
                col[i] = max(col[i], grid[i][j])
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(col[i], row[j]) - grid[i][j]
        return res
