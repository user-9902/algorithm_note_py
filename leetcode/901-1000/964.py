"""
@title:      964. 表示数字的最少运算符
@difficulty: 中等
@importance: 4/5
@tags:       记忆化搜索 快速幂
"""
from functools import cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
        @tags:              记忆化搜索 快速幂
        @time complexity:   O(logxtarget)
        @space complexity:  O(logtarget)
        """
        @cache
        def dfs(n):
            if n <= x:
                return min(2 * (x - n), 2 * n - 1)

            cnt = 0
            cur = x
            while cur < n:
                cur *= x
                cnt += 1
            # 刚好
            if cur == n:
                return cnt

            res = dfs(n - (cur // x)) + cnt
            if cur - n < n:
                res = min(res, dfs(cur - n) + cnt + 1)
            return res

        return dfs(target)


Solution().leastOpsExpressTarget(3, 5)
