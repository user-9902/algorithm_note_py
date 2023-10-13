"""
50. Pow(x, n)
快速幂，二进制
2^13 = 2^(0b1101) = 2^8 * 2^4 * 2^1
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        ans = 1
        while m:
            if m & 1:
                ans *= x
            x *= x
            m >> 1
        return ans if n > 0 else 1 / ans