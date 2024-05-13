"""
36. 有效的数独
设计题目
如何高效的查重
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        bf
        """
        def is_legal(i, j, s):
            for x in range(9):
                if x == j:
                    continue
                if board[i][x] == s:
                    return False

            for x in range(9):
                if x == i:
                    continue
                if board[x][j] == s:
                    return False

            a = i // 3
            b = j // 3
            for x in range(a*3, a*3+3):
                for y in range(b*3, b*3+3):
                    if x == i and y == j:
                        continue
                    if board[x][y] == s:
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if not is_legal(i, j, board[i][j]):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        hash map + 位运算
        这里将位运算作为map以减少内存开销
        map 为 2^1 + 2^2 + 2^3 ... + 2^9 = 1023
        """
        # 0：行 1：列 2：方块
        board_map = [[1023] * 9 for _ in range(3)]

        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s == '.':
                    continue
                n = int(s)

                if (board_map[0][j] >> n) % 2 == 1:
                    board_map[0][j] ^= 2 ** n
                else:
                    return False

                if (board_map[1][i] >> n) % 2 == 1:
                    board_map[1][i] ^= 2 ** n
                else:
                    return False

                if (board_map[2][(i // 3 * 3) + j // 3] >> n) % 2 == 1:
                    board_map[2][(i // 3 * 3) + j // 3] ^= 2 ** n
                else:
                    return False

        return True


res = Solution().isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                  "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
)
print(res)

str
