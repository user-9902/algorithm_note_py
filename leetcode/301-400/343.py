"""
@title:      343. 整数拆分
@difficulty: 中等
@importance: 4/5
@tags:       dp 打表
"""

f = [0] * 59
f[2] = 1
f[3] = 2
f[4] = 4
for i in range(5, 59):
    for j in range(1, (i // 2) + 1):
        # 这里在 2个数相乘  >2个数相乘 中挑选最大值
        f[i] = max((i - j) * j, f[i - j] * j, f[i])


class Solution:
    def integerBreak(self, n: int) -> int:
        return f[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(m*n)
        @space complexity:  O(m*n)
        @description:       f[i] = max((i - j) * j, f[i - j] * j, f[i]) 其中 j < i//2
        """
        return f[n]
