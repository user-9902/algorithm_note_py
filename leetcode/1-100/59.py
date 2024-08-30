"""
@title:      59. 螺旋矩阵 II
@difficulty: 简单
@importance: 3/5
@tags:       模拟 
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        @tags:              模拟
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       打圈。简化版的 leetcode 54
        """
        matrix = [[0] * n for _ in range(n)]
        v = 1
        # 能完整打圈的次数
        for i in range(n // 2):
            for x in range(n - i * 2 - 1):
                matrix[i][x + i] = v
                v += 1

            for x in range(n - i * 2 - 1):
                matrix[i + x][n - 1 - i] = v
                v += 1

            for x in range(n - i * 2 - 1):
                matrix[n - 1 - i][n - i - 1 - x] = v
                v += 1

            for x in range(n - i * 2 - 1):
                matrix[n - 1 - i - x][i] = v
                v += 1

        if n % 2:
            matrix[(n // 2)][(n // 2)] = v
        return matrix
