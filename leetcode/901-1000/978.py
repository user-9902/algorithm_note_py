"""
@title:      978. 最长湍流子数组
@difficulty: 简单
@importance: 3/5
@tags:       线性dp
"""
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       f[i][0] 下面需要 >arr[i-1]  f[i][1] 下面需要 <arr[i-1]
        """
        n = len(arr)
        f = [[1, 1] for _ in range(n)]
        res = 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                # f[i][0] 下面需要 >
                f[i][1] = f[i-1][0] + 1
                res = max(res, f[i][1])
            if arr[i] < arr[i-1]:
                # f[i][1] 下面需要 <
                f[i][0] = f[i-1][1] + 1
                res = max(res, f[i][0])
        return res
