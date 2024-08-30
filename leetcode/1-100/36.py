"""
@title:      36. 有效的数独
@difficulty: 中等
@importance: 3/5
@tags:       状态压缩
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        @tags:              二进制状态压缩
        @time complexity:   O(n) 空格数量
        @space complexity:  O(n*n)
        @description:       二进制压缩状态校验同行 同列 同3*3矩阵 是否重复  leetcode 37前置题
        """
        u = (1 << 9) - 1
        col = [u] * 9
        row = [u] * 9
        mat = [u] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    b = 1 << (int(board[i][j]) - 1)
                    idx = (i // 3) * 3 + (j // 3)
                    if col[j] & b == 0 or row[i] & b == 0 or mat[idx] & b == 0:
                        return False
                    col[j] ^= b
                    row[i] ^= b
                    mat[idx] ^= b
        return True
