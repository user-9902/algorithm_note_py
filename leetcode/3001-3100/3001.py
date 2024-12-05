"""
@title:      3001. 捕获黑皇后需要的最少移动次数
@difficulty: 中等
@importance: 5/5
@tags:       脑筋急转弯
"""


class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        """
        @tags:              脑筋急转弯
        @time complexity:   O(1)   
        @space complexity:  O(1)
        @description:       同一条直线上掣肘的情况分析下即可
        """
        if a == e:
            if a == c and (b > d > f or b < d < f):
                return 2
            return 1
        if b == f:
            if b == d and (a > c > e or a < c < e):
                return 2
            return 1
        if e + f == c + d:
            if e + f == a + b and (e < a < c or e > a > c):
                return 2
            return 1
        if f - e == d - c:
            if f - e == b - a and (e < a < c or e > a > c):
                return 2
            return 1
        return 2
