"""
解数独
状态压缩，状态指的是：未填数字的可能性状态。压缩指的是：用填入了的数，去压缩未确定数的可能性。
状态回溯，当存在无法靠压缩完成的情况时，就需要猜一个数，猜错了则需要回溯。
优化一：
未填入的数的可能状态，用位存储的方式以节省空间
E.g
    cur = 268 = 256 | 8 | 4 = 2^8 | 2^3 | 2^2
    cur 可能为 [8, 4, 2]中的一个
优化二：
压缩过了的数就无需再次重复压缩，用一张9*9的list保存即可
"""
from typing import List

# 位运算存储信息
BIT_MAP = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)


class Solution:
    def status_compress(self, board: List[List[str]], table: List[List[bool]]) -> (int, int):
        # 压缩可能性的方法
        compress_counter = 0   # 压缩次数
        fill_in_counter = 0  # 填入次数
        for i in range(9):
            for j in range(9):
                if table[i][j]:
                    continue

                cur = board[i][j]
                if type(cur) == int:
                    # 可能的状态只有一种时，数字就可以填入了
                    if cur in BIT_MAP:
                        board[i][j] = str(BIT_MAP.index(cur))
                        fill_in_counter += 1
                    continue

                # 行压缩
                for row in range(9):
                    if type(board[row][j]) == int:
                        board[row][j] &= ~BIT_MAP[int(cur)]
                        compress_counter += 1

                # 列压缩
                for colum in range(9):
                    if type(board[i][colum]) == int:
                        board[i][colum] &= ~BIT_MAP[int(cur)]
                        compress_counter += 1

                # 3 * 3 方格压缩
                for m in range(3):
                    for n in range(3):
                        x = (i // 3) * 3 + m
                        y = (j // 3) * 3 + n
                        if type(board[x][y]) == int:
                            board[x][y] &= ~BIT_MAP[int(cur)]
                            compress_counter += 1

                # 标记未压缩过了，后续的迭代就无需再次压缩
                table[i][j] = True
        return (compress_counter, fill_in_counter)

    def is_legal(self, board: List[List[int]], row: int, col: int, val: str) -> bool:
        for i in range(9):
            if type(board[row][i]) == str and board[row][i] == val:
                return False

        for i in range(9):
            if type(board[i][col]) == str and board[i][col] == val:
                return False

        for i in range((row // 3) * 3, (row // 3) * 3 + 3):
            for j in range((col // 3) * 3, (col // 3) * 3 + 3):
                if type(board[i][j]) == str and board[i][j] == val:
                    return False
        return True

    def dfs(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if type(cur) == str:
                    continue
                # 已经修剪过可能性了，因此无需遍历1-9
                for k in range(1, 10):
                    if cur & BIT_MAP[k] != 0:
                        if self.is_legal(board, i, j,  str(k)):
                            board[i][j] = str(k)
                            if self.violent_enumeration(board):
                                return True
                            # 状态回溯
                            board[i][j] = cur
                # 非法填入，则直接中断，既修剪掉该分支的剩余可能性。
                return False
        # 遍历完整个数独仍然，依然合法，则说明找到了解。
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        rest = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 1022
                    rest += 1
        table = [[False]*9 for i in range(9)]

        # 压缩状态。
        # 部分数独可以只靠该状态压缩方法，得到解。
        # 无法通过该方法得到解的数独，需要使用回溯算法解决。
        while rest > 0:
            (c, f) = self.status_compress(board, table)
            rest -= f
            if c == 0 and f == 0:
                break

        # 回溯。
        # 无法只靠压缩状态完成时。
        # 上面压缩状态的步骤也可以帮助我们修剪可能性。
        if rest > 0:
            # dfs回溯
            self.dfs(board)
