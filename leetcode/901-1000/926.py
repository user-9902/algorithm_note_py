"""
@title:      926. 将字符串翻转到单调递增
@difficulty: 中等
@importance: 4/5
@tags:       前缀和 dp
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        @tags:              前缀和 fs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       遍历分割点，分割点左侧为0，右侧全为1，计算最小转化次数
        """
        n = len(s)
        pre = [0] * n
        for i in range(n):
            if i > 0:
                pre[i] = pre[i-1]
            if s[i] == '1':
                pre[i] += 1

        res = min(pre[-1], n-pre[-1])

        for i in range(1, n):
            cur = pre[i-1] + (n - i - pre[-1] + pre[i-1])
            res = min(res, cur)

        return res

    def minFlipsMonoIncr(self, s: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n) 可压缩空间复杂度至O(1)
        @description:       f1[i] 表示前i个元素，以0结尾时的最少反转次数；f2[i] 表示前i个元素，以1结尾时的最少反转次数。
        """
        n = len(s)
        f1 = [0] * n  # 以 0 结尾
        f2 = [0] * n  # 以 1 结尾
        f1[0] = 1 if s[0] == "1" else 0
        f2[0] = 1 if s[0] == "0" else 0
        for i in range(1, n):
            # 0结尾 前面都得是0
            f1[i] = f1[i - 1] + (1 if s[i] == "1" else 0)
            # 1结尾 前面可以是0或1
            f2[i] = min(f2[i - 1], f1[i - 1]) + (0 if s[i] == "1" else 1)
        return min(f1[n - 1], f2[n - 1])
