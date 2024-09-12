"""
@title:      119. 杨辉三角 II
@difficulty: 中等
@importance: 4/5
@tags:       dp 杨辉三角
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       模拟每层数字计算的过程
        """
        f = [[0] * (rowIndex + 1) for _ in range(rowIndex + 1)]
        f[0][0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i + 1):
                if j == 0 or j == i:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i - 1][j] + f[i - 1][j - 1]
        return f[rowIndex][: rowIndex + 1]
