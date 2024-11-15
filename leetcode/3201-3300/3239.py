"""
@title:      3239. 最少翻转次数使二进制矩阵回文 I
@difficulty: 简单
@importance: 2/5
@tags:       双指针
"""

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        """
        @tags:              双指针
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       分别计算 横向的反转次数 纵向的反转次数 即可
        """
        n, m = len(grid), len(grid[0])
        a = 0
        for i in range(n):
            l = 0
            r = m - 1
            while l < r:
                if grid[i][l] != grid[i][r]:    # 可用异或运算优化
                    a += 1
                l += 1
                r -= 1
        z = 0
        for j in range(m):
            t = 0
            b = n - 1
            while t < b:
                if grid[t][j] != grid[b][j]:
                    z += 1
                t += 1
                b -= 1
        return min(a, z)


Solution().minFlips([[0, 1], [0, 1], [0, 0]])
