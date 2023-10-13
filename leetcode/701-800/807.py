"""
807. 保持城市天际线
数组
辣鸡题
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        不能超过同行最高，同列最高中的小值
        """
        n = len(grid)
        max_row = []
        max_clo = []
        ans = 0
        for i in range(n):
            max_row.append(max(grid[i]))
            clo = 0
            for j in range(n):
                clo = max(clo, grid[j][i])
            max_clo.append(clo)

        for i in range(n):
            for j in range(n):
                r = min(max_row[i], max_clo[j]) - grid[i][j]
                ans += r if r > 0 else 0
        return ans


Solution().maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
