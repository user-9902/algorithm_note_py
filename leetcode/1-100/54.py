"""
54. 螺旋矩阵
设计
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        打圈儿
        """
        top = 0
        n = len(matrix)
        m = len(matrix[0])

        ans = []
        while min(m-top, n-top) // 2 > 0:
            for i in range(top, m-1):
                ans.append(matrix[top][i])

            for i in range(top, n-1):
                ans.append(matrix[i][m-1])

            for i in range(m-1, top, -1):
                ans.append(matrix[n-1][i])

            for i in range(n-1, top, -1):
                ans.append(matrix[i][top])

            top += 1
            m -= 1
            n -= 1

        if n - top == 1:
            for i in range(top, m):
                ans.append(matrix[(n+top) // 2][i])
        elif m - top == 1:
            for i in range(top, n):
                ans.append(matrix[i][(m+top) // 2])

        return ans


Solution().spiralOrder(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
