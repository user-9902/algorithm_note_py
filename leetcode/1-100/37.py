"""
@title:      37. 解数独
@difficulty: 中等
@importance: 4/5
@tags:       dfs 回溯 状态压缩
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        @tags:              回溯 dfs 二进制状态压缩
        @time complexity:   O(9^k) 空格数量
        @space complexity:  O(k)
        @description:       dfs 回溯
        """
        # 位运算状态压缩
        u = (1 << 9) - 1

        col = [u] * 9   # 列中剩余元素
        row = [u] * 9   # 行中剩余元素
        mat = [u] * 9   # 3*3中剩余元素

        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s != ".":
                    b = int(s) - 1
                    row[i] ^= 1 << b
                    col[j] ^= 1 << b
                    mat[i // 3 * 3 + j // 3] ^= 1 << b

        # 当前选的元素是否能填入
        def is_legal(i, j):
            s = board[i][j]
            b = int(s) - 1
            return (
                row[i] >> b & 1
                and col[j] >> b & 1
                and mat[i // 3 * 3 + j // 3] >> b & 1
            )

        res = None

        def dfs(i, j):
            nonlocal res
            if i == 9:
                res = [i.copy() for i in board]
                return
            s = board[i][j]
            if s == ".":
                for x in range(1, 10):
                    y = str(x)
                    board[i][j] = y
                    if is_legal(i, j):
                        b = x - 1
                        row[i] ^= 1 << b
                        col[j] ^= 1 << b
                        mat[i // 3 * 3 + j // 3] ^= 1 << b

                        dfs(i + ((j + 1) // 9), (j + 1) % 9)

                        row[i] ^= 1 << b
                        col[j] ^= 1 << b
                        mat[i // 3 * 3 + j // 3] ^= 1 << b
                    board[i][j] = "."
            else:
                dfs(i + ((j + 1) // 9), (j + 1) % 9)

        dfs(0, 0)
        for i in range(9):
            board[i] = res[i]


Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
    "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
