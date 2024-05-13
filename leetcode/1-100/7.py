"""
7. 整数反转
difficulty: 简单
importance: 4/5
tags:       数学
"""


class Solution:
    def reverse(self, x: int) -> int:
        x_abs = abs(x)
        ans = 0
        max = 2**31

        while x_abs > 0:
            ans *= 10
            ans += x_abs % 10
            x_abs //= 10
            if ans > max:
                return 0

        return ans if x > 0 else -ans
