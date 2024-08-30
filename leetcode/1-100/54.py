"""
@title:      54. 螺旋矩阵
@difficulty: 中等
@importance: 4/5
@tags:       模拟 
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        @tags:              模拟
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       打圈，然后处理剩余无法打圈的
        """
        n, m = len(matrix), len(matrix[0])
        ans = []
        r = 0
        # 能完整打圈的次数
        for i in range(min(n // 2, m // 2)):
            r += 1
            for x in range(m - i * 2 - 1):
                ans.append(matrix[i][x + i])

            for x in range(n - i * 2 - 1):
                ans.append(matrix[i+x][m - 1 - i])

            for x in range(m - i * 2 - 1):
                ans.append(matrix[n - 1 - i][m - i - 1 - x])

            for x in range(n - i * 2 - 1):
                ans.append(matrix[n - 1 - i - x][i])

        # 处理剩余的
        # 行高 且存在剩余 竖着打印剩余的
        if n >= m and m % 2:
            for j in range(r, n-r):
                ans.append(matrix[j][r])
        # 横着的剩余
        if m > n and n % 2:
            for j in range(r, m-r):
                ans.append(matrix[r][j])
        return ans
