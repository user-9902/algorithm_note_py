"""
51. N 皇后
dfs问题。
在dfs遍历的时候，修剪掉不可能的状态。分别需要修剪列，对角线，反对角线

参考自 https://www.bilibili.com/video/BV17L4y1g7es/?spm_id_from=333.788&vd_source=51614d2a49bfb1ec0bdf64b53b2dacd5
列重复很容易想到，而截距重复实在是精妙
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        stage = ['.'*n]*n
        res = []
        col = [False] * n  # 当前列上是否有棋子
        dg = [False] * 2 * n  # 当前斜线上是否有棋子 y = x + n
        udg = [False] * 2 * n  # 当前反斜杠上是否已经有棋子 y = -x + n

        def dfs(x: int):
            print(x, n)
            if x == n:
                # 最后一个棋子能放入即是一种解
                res.append(True)
            for y in range(n):
                if col[y] or dg[y + x] or udg[y - x + n]:
                    continue
                col[y] = dg[y + x] = udg[y - x + n] = True
                stage[x] = '.'*y + 'Q' + '.'*(n - y - 1)
                dfs(x + 1)  # 遍历下一行
                # 状态回溯
                stage[x] = '.'*n
                col[y] = dg[y + x] = udg[y - x + n] = False

        dfs(0)
        return len(res)


Solution().solveNQueens(n=4)
