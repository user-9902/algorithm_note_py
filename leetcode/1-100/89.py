"""
@title:      89. 格雷编码
@difficulty: 中等
@importance: 3/5
@tags:       格雷编码
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        @tags:              回溯 剪枝
        @time complexity:   O(n2^n)   
        @space complexity:  O(1)
        @description:       能通过 但并非题目的考察本意
        """
        res = None
        cur = [0]
        cnt = (1 << n) - 1  # 1-u个数
        s = (1 << cnt) - 1

        def dfs(u, i):
            nonlocal res
            if u == 0:
                if (cur[0] ^ cur[-1]).bit_count() == 1:
                    res = cur.copy()
                return
            if res:
                return
            for j in range(n):
                v = (1 << j) ^ cur[i - 1]
                if v > 0 and (1 << (v - 1)) & u:
                    cur.append(v)
                    dfs(u ^ (1 << (v - 1)), i + 1)
                    cur.pop()

        dfs(s, 1)
        return res

    def grayCode(self, n: int) -> List[int]:
        """
        @tags:              格雷编码
        @time complexity:   O(2^n)   
        @space complexity:  O(1)
        @description:       后一项照着前一项推导，前一项添加前缀0,生成轴对称的添加前缀1
                            1:  0 | 1
                            2:  00  01 | 11  10
                            3:  000 001 011 010 | 110 111 101 100
        """
        m = 2 ** n
        arr = [0] * m
        arr[1] = 1
        for i in range(2, n+1):
            v = 1 << (i-1)
            cnt = 2**(i-1)
            for j in range(cnt):
                pre = cnt - j - 1
                arr[cnt + j] = arr[pre] ^ v
        return arr
