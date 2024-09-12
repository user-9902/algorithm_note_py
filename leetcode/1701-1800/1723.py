"""
@title:      1723. 完成所有工作的最短时间
@difficulty: 中等
@importance: 5/5
@tags:       状压dp
"""

from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        @tags:              状压dp
        @time complexity:   O(3^n)
        @space complexity:  O(2^n)
        @description:       将题意抽象为，将数组分为 k 组，如何使得所有分组中的和最大值最小。
                            f[i][k] = min(max(f[i^s][k-1],sum(s)))。 (s ∈ i
                            💲状压模板题。当答案与输入无关，有集合的划分，消耗的概念时，就可以联想到状压dp了
        """
        n = len(jobs)
        u = 1 << n
        sums = [0] * u
        #  00 01 10 11 100 101 110 111
        for i, v in enumerate(jobs):
            idx = 1 << i
            for j in range(idx):
                sums[idx | j] = sums[j] + v

        f = sums.copy()
        # f[i][k] = f[i^s][k-1] 撇除当前集合
        for _ in range(1, k):
            # j 表示当前需要分析的总集合 f[i]
            # 这里压缩至了一维，从后向前遍历，防止状态的错误覆盖
            # 未压缩至一维的实现，见 leetcode 2305
            for j in range(u - 1, 0, -1):
                # t 表示当前选取的集合
                t = j
                while t:
                    # 除去当前选的 子问题
                    v = f[j ^ t]
                    if sums[t] > v:  # 💲不用 min max 减少函数栈的开销
                        v = sums[t]
                    if v < f[j]:
                        f[j] = v
                    # 遍历当前总集合数 j 的所有子集
                    t = (t - 1) & j
        return f[u - 1]
