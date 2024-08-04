"""
@title:      509. 斐波那契数
@difficulty: 简单
@importance: 5/5
@tags:       dp 迭代
"""

from functools import cache


class Solution:
    def fib(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(2^n)
        @space complexity:  O(1)
        @description:       朴素的迭代解法
        """
        # 朴素的解法时间复杂度太高 2 -> 2 3 -> 6 4 -> 14 5 -> 30
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    def fib(self, n: int) -> int:
        """
        @tags:              迭代 + cache
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       如我们在计算 fib(5) 时 需要计算 f(3) 和 f(4)。而f(4)需要f(3)，可以发现这里需要重复计算f(3)。我们将过去计算的步骤保存下来就可以极大的降低计算的复杂度。 
        """
        @cache
        def fib(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return fib(n-1) + fib(n-2)
        return fib(n)

    def fib(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       可以发现上述的迭代是从 n -> 0 进行推导，而当我们从0 -> n进行递推的时候，便是dp
        """
        if n < 1:
            return 0

        f = [0] * (n + 1)
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

    def fib(self, n: int) -> int:
        """
        @tags:              dp + 优化空间复杂度
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       n 只依赖于 n-1 n-2 的状态，因此我们不需要那么多的空间来缓存数据
        """
        f = [0, 1]
        for i in range(2, n + 1):
            f[i % 2] = f[0] + f[1]
        return f[n % 2]
