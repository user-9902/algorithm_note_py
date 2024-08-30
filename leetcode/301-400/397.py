"""
@title:      397. 整数替换
@difficulty: 中等
@importance: 5/5
@tags:       dfs bfs greedy
"""

from functools import cache


class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        @tags:              bfs
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)  可用记忆化搜索优化
        @description:       bfs
        """
        stack = [n]

        l = 0
        while stack:
            n = len(stack)
            for i in range(n):
                cur = stack.pop(0)
                if cur == 1:
                    return l
                if cur % 2 == 0:
                    stack.append(cur // 2)
                else:
                    stack.append(cur + 1)
                    stack.append(cur - 1)
            l += 1

    def integerReplacement(self, n: int) -> int:
        """
        @tags:              bfs
        @time complexity:   O(logn)
        @space complexity:  O(logn)
        @description:       bfs
        """
        @cache
        def bfs(n, step):
            if n == 1:
                return step
            if n % 2 == 0:
                return bfs(n//2, step + 1)
            else:
                return min(bfs(n-1, step+1), bfs(n+1, step+1))
        return bfs(n, 0)

    def integerReplacement(self, n: int) -> int:
        """
        @tags:              greedy
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       从二进制的角度分析
                            需要将 n 变为 1。即将二进制的 n 变为 0001
                            偶数 1101010 只能右移动
                            奇数 1101011 可 + 1 或 - 1。
                                -1 需要两步才能右移。
                                +1 也需要两部才能右移一位，但 +1 存在进位，则可能将右侧的1变为0
                                末尾为 01 时候需-1 其余 + 1
        """
        res = 0
        while n > 1:
            if n % 2 == 1:
                # 3 是个例外
                if n >> 1 & 1 == 0 or n == 3:
                    n -= 1
                else:
                    n += 1
            else:
                n >>= 1
            res += 1
        return res
