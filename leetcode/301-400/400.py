"""
@title:      400. 第 N 位数字
@difficulty: 中等
@importance: 4/5
@tags:       math
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        @tags:              fs 位运算优化
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       1位数字个数 9 个    1 ... 9        1-9
                            2位数字个数 90 个   10 ... 99      10-189
                            3位数字个数 900 个  100 ... 999    190-2889
                            ...
        """
        if n < 10:
            return n
        m = 9
        f = [9] * m
        for i in range(1, m):
            f[i] = (i + 1) * 9 * 10**i + f[i - 1]
        i = 8
        # 是几位数
        while n < f[i]:
            i -= 1
        # 能完整覆盖的最后一个数字
        a = 10 ** (i + 1) + (n - f[i]) // (i + 2) - 1
        # 余数
        idx = (n - f[i]) % (i + 2)
        return a % 10 if idx == 0 else int(str(a + 1)[idx - 1])
