"""
@title:      354. 俄罗斯套娃信封问题
@difficulty: 中等
@importance: 4/5
@tags:       LIS dp
"""

from bisect import bisect_left
from typing import List
from math import inf


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        @title:             dp
        @time complexity:   O(n^2) ❌ 时间复杂度超了 观察数据规模也可以知道 n^2 的时间复杂度会超
        @space complexity:  O(n)  
        """
        envelopes.sort()
        n = len(envelopes)
        f = [1] * n

        for i in range(n):
            for j in range(i):
                if (
                    envelopes[i][0] > envelopes[j][0]
                    and envelopes[i][1] > envelopes[j][1]
                ):
                    f[i] = max(f[i], 1 + f[j])
        return max(f)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        @title:             LIS
        @time complexity:   O(nlogn)
        @space complexity:  O(n)  
        @description:       见下方
        """
        # 最关键的就是这里的排序，宽相同的时候，高度倒序排列，确保了同宽的信封不会出现在递增子序列中
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        stack = [envelopes[0][1]]

        # 宽度已经有序，高度算出递增子序列即可
        for i in range(1, n):
            cur = envelopes[i]
            l = 0
            r = len(stack)
            if cur[1] > stack[r - 1]:
                stack.append(cur[1])
            else:
                while l < r:
                    mid = (l + r) >> 1
                    if stack[mid] < cur[1]:
                        l = mid + 1  # [mid+1, r)
                    else:
                        r = mid  # [l,mid)
                stack[l] = cur[1]
        return len(stack)
